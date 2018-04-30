# -*- coding: utf-8 -*-

import time
import json
import memcache


def memcache_tt():
    mc = memcache.Client([("192.168.1.131:11211", 2)], debug = True)

    t1 = time.time()
    loops = 0
    while loops < 1000:
        mc.set("user", "jason" + str(loops))
        loops += 1
    print("using time", time.time() - t1)

    print(mc.get("user"))


def memcache_json():
    user_info = {"name" : "hongjianan",
                 "age" : 27,
                 "gender" : 1,
                 "imgs": ["1.jpg", "2.jpg"]}
    user_id = "1"
    user_list = ["1", "2", "3"]

    mc = memcache.Client([("192.168.1.131:11211", 2)], debug = True)
    mc.set("user_list", json.dumps(user_list))

    j = json.dumps(user_info)
    print(type(j), j)
    mc.set(user_id, j)
    ret = mc.get(user_id)
    print(ret)
    info = json.loads(ret, encoding = "utf-8")
    print(type(info), info)
    print(info["imgs"])


def run():
    # memcache_tt()
    memcache_json()


if __name__ == "__main__":
    run()
    

