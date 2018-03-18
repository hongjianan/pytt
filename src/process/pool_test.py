# coding: UTF-8

import time
from multiprocessing import Pool


def worker(idx):
    print("worker start %s" % idx)
    time.sleep(2)
    print("worker end %s" % idx)
    return idx


def end_work(arg):
    print("end_work %s" % arg)


def pool_tt():
    pool = Pool(5)
    for i in range(10):
        # pool.apply(func = worker, args = (i,))  # 同步阻塞调用
        pool.apply_async(func = worker, args = (i,), callback = end_work) # 异步非阻塞调用

    print("pool call end")
    pool.close()
    pool.join()


def run():
    pool_tt()


if __name__ == "__main__":
    run()
    

