# coding: utf-8

import threading
import time
from Queue import Queue


class ThreadProducer(threading.Thread):
    def __init__(self, thread_name, queue, max_times):
        super(ThreadProducer, self).__init__()
        self.thread_name = thread_name
        self.times = max_times
        self.queue = queue

    def producer(self, times):
        print("+++[%s][%d]" % (self.thread_name, times))
        self.queue.put({self.thread_name : times})


    def run(self):
        print("ThreadProducer[%s] start ..." % self.thread_name)

        times = 0
        while times < self.times:
            time.sleep(1)
            self.producer(times)
            times += 1


class ThreadConsumer(threading.Thread):
    def __init__(self, thread_name, queue, try_times):
        super(ThreadConsumer, self).__init__()
        self.thread_name = thread_name
        self.try_times = try_times
        self.queue = queue

    def consumer(self):
        data = self.queue.get(False)
        print("--[%s]" % self.thread_name, data)


    def run(self):
        print("ThreadConsumer[%s] start ..." % self.thread_name)

        try_times = 0
        while try_times < self.try_times:
            time.sleep(1)
            try:
                self.consumer()
                try_times = 0
            except:
                print("queue no data", try_times)
                try_times += 1


def run():
    queue = Queue(20)
    p1 = ThreadProducer("p1", queue, 10)
    p2 = ThreadProducer("p2", queue, 3)
    c1 = ThreadConsumer("c1", queue, 3)

    # 设置为 前台线程 进程会等待所有线程结束之后再退出， 模式就是前台线程
    # p1.setDaemon(False)
    # p2.setDaemon(False)
    # c1.setDaemon(False)

    p1.start()
    p2.start()
    c1.start()

    # for thread in (p1, p2, c1):
    #     thread.join()

    print("main thread exit ...")


if __name__ == "__main__":
    run()
