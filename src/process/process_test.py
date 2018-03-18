# coding: UTF-8

import sys
import time
from multiprocessing import Process, Value, Array


def worker(name, value, arr):
    value.value = 100
    for i in range(len(arr)):
        arr[i] = -arr[i]
        print("{} loop={}".format(name, i))
        time.sleep(1)


def process_tt():
    # 共享内存支持, 但是 Value, Array限制太多，提倡用 Manager.dict()
    value = Value("d", 1)
    arr = Array("i", range(100))

    print(value)
    print(arr[:])

    procs = []
    procs.append(Process(target = worker, args = ("proc_test1", value, arr)))

    # for p in procs:
    #     p.daemon = True   # 默认False，主进程终止，子进程也退出

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    print(value)
    print(arr[:])


def run():
    process_tt()


if __name__ == "__main__":
    run()

