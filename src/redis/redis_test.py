# -*- coding: utf-8 -*-

import time
import redis


def redis_tt():
    try:
        rds = redis.StrictRedis(host = "192.168.1.131", password = "hong")
    except Exception as e:
        print("connect redis failed", e)
        return -1
    else:
        print("connect redis successful")

    t1 = time.time()
    for i in range(1000):
        rds.set("user", "jason" + str(i))
    print("using time", time.time() - t1)

    print(rds.get("user"))


def pipeline_tt():
    try:
        rds = redis.StrictRedis(host = "192.168.1.131", password = "hong")
    except Exception as e:
        print("connect redis failed", e)
        return -1
    else:
        print("connect redis successful")
    pipe = rds.pipeline()

    t1 = time.time()
    for i in range(1000):
        pipe.set("user", "jason" + str(i))
    # pipe.execute()
    print("pipeline using time", time.time() - t1)

    print(rds.get("user"))


def run():
    # redis_tt()
    pipeline_tt()


if __name__ == "__main__":
    run()
    

