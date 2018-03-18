# coding: UTF-8

import time
import datetime


def time_tt():
    # time()
    t0 = time.time()
    print(type(t0), t0)
    time.sleep(1)
    print(time.time())

    # ctime
    print(time.ctime())
    print(time.ctime(t0 - 3600))

    # gmtime()
    tm_obj = time.gmtime()
    print(type(tm_obj), tm_obj)
    print("%d-%d-%d" % (tm_obj.tm_year, tm_obj.tm_mon, tm_obj.tm_mday))
    print("%s-%s-%s %s" % (tm_obj.tm_year, tm_obj.tm_mon, tm_obj.tm_mday, tm_obj.tm_hour))


def run():
    time_tt()


if __name__ == "__main__":
    run()
    

