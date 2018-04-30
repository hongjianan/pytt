# -*- coding: utf-8 -*-

from multiprocessing import Process, Manager


def worker(dit, key, value):
    dit[key] = value


def manager_tt():
    manager = Manager()
    dit = manager.dict()
    dit[1] = "one"

    print(dit)
    p = Process(target = worker, args = (dit, 2, "two"))
    p.start()
    p.join()

    print(dit)


def run():
    manager_tt()


if __name__ == "__main__":
    run()
    

