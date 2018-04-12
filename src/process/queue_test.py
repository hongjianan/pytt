# coding: UTF-8

# Queue底层实现是 pipe

import os, time
import multiprocessing


def proc_consumer(queue):
    for i in range(1000):
        value = queue.get()
        print("get", value)
        time.sleep(2)


def queue_tt():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target = proc_consumer, args = (q,))
    p1.start()

    for i in range(1000):
        q.put(i)
        print("put", i)
        time.sleep(1)



def run():
    queue_tt()


if __name__ == "__main__":
    run()
    

