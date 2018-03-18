# coding: UTF-8

import time
import memcache


def cas_multi_client():
    mc1 = memcache.Client(["192.168.1.131:11211"], debug = True, cache_cas = True)
    mc2 = memcache.Client(["192.168.1.131:11211"], debug = True, cache_cas = True)
    mc1.set_multi({"user": "jason", "age": 10})

    age1 = mc1.gets("age")
    age2 = mc2.gets("age")
    print(age1, age2)

    mc1.cas("age", age1 + 1)
    mc2.cas("age", age2 + 1)

    print(mc1.gets("age"))


def cas_one_client():
    mc = memcache.Client(["192.168.1.131:11211"], debug = True, cache_cas = True)
    mc.set_multi({"user":"jason", "age":10})
    age = mc.gets("age")
    print(age)
    mc.set("age", age + 1)
    mc.set("age", age + 2)
    print(mc.gets("age"))

    mc.cas("age", age + 3)
    mc.cas("age", age + 4)
    print(mc.gets("age"))


def run():
    # cas_multi_client()
    cas_one_client()


if __name__ == "__main__":
    run()
    

