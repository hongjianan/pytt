# -*- coding: utf-8 -*-
'''
Created on 2018年8月6日

@author: Hong
'''
import time
from cacheout import Cache


def cache_tt():
    cache = Cache(maxsize=2, ttl=2)
    cache.set(1, 'one')
    print(cache.get(1))
    time.sleep(3)
    print(cache.get(1))


if __name__ == '__main__':
    cache_tt()
