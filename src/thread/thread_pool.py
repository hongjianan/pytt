# coding: UTF-8

import time
from Queue import Queue
import threading


class ThreadPool(object):
    """
    简单线程池
    """
    def __init__(self, max_size):
        self.__thread_size = max_size
        self.__runable = True
        self.__ready_pool()

    def __ready_pool(self):
        self.__task_queue = Queue()     # 任务队列
        self.__thread_list = []        # 线程列表
        self.__free_threads = 0         # 空闲线程数
        self.__lock = threading.RLock()

    def add_free(self, incr = 1):
        self.__lock.acquire()
        self.__free_threads += incr
        self.__lock.release()

    def sub_free(self, desc = 1):
        self.__lock.acquire()
        self.__free_threads -= desc if self.__free_threads > 0 else 0
        self.__lock.release()

    def __thread_worker(self, id):
        first_flag = True

        while (self.__runable) or (not self.__task_queue.empty()):
            fun_args = self.__task_queue.get(timeout = 1)
            if fun_args:
                timestamp = fun_args[0]
                print(timestamp, time.time())
                func = fun_args[1]
                cb   = fun_args[2]
                args = fun_args[3]

                print("__thread_worker run id=%d" % id)
                if time.time() - timestamp > 2:
                    print("task over time=%s, drop it" % timestamp)
                    continue

                if callable(func):
                    # 这里这么写是为了连续调用 run()时，先加了free,导致后面的run()不创建thread
                    if first_flag:
                        first_flag = False
                    else:
                        self.sub_free()

                    ret = func(*args)
                    if callable(cb):
                        cb(ret)

                    self.add_free()
                    print(self.free_threads())
                else:
                    print("input func is not callable")

        self.sub_free()
        del self.__thread_list[id]

    def free_threads(self):
        return self.__free_threads

    def run(self, target, args = (), callback = None):
        self.__task_queue.put((time.time(), target, callback, args))

        print("thread free=%d total=%d" % (self.free_threads(), len(self.__thread_list)))
        if (not self.free_threads()) and (len(self.__thread_list) < self.__thread_size):
            print("thread free=%d total=%d, need create thread" % (self.free_threads(), len(self.__thread_list)))
            t = threading.Thread(target = self.__thread_worker, args = (len(self.__thread_list),))
            t.start()
            self.__thread_list.append(t)

    def close(self):
        self.__runable = False


def print_value(value):
    print("print_num %s" % value)
    time.sleep(1)
    return value


def print_key_value(key, value):
    print("print_num %s=%s" % (key, value))
    time.sleep(1)
    return value


def end_print(value):
    print("end_print %s" % value)


def pool_tt():
    pool = ThreadPool(2)

    for i in range(5):
        if i % 2:
            pool.run(target = print_value, callback = end_print, args = (i,))
        else:
            pool.run(target = print_key_value, callback = end_print, args = (i, i+1))

    pool.close()


def run():
    pool_tt()


if __name__ == "__main__":
    run()
