# coding: UTF-8

import threading
import time

INCR_NUM = 0
LOCK = threading.RLock()


def thread_unsafe_add():
    global INCR_NUM

    loops = 0
    while loops < 1000 * 100:
        loops += 1
        INCR_NUM += 1


def thread_safe_add():
    global INCR_NUM

    loops = 0
    while loops < 1000 * 100:
        loops += 1
        LOCK.acquire()
        INCR_NUM += 1
        LOCK.release()


def lock_tt():
    global INCR_NUM

    t1 = threading.Thread(target = thread_unsafe_add)
    t2 = threading.Thread(target = thread_unsafe_add)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(INCR_NUM, INCR_NUM == 2 * 1000 * 100)
    print("=====================")

    INCR_NUM = 0
    t1 = threading.Thread(target = thread_safe_add)
    t2 = threading.Thread(target = thread_safe_add)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(INCR_NUM, INCR_NUM == 2 * 1000 * 100)


def run():
    lock_tt()


if __name__ == "__main__":
    run()
