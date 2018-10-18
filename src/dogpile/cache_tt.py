# -*- coding: utf-8 -*-
'''
Created on 2018年9月6日

@author: Administrator
'''
import time
from dogpile.cache import make_region

BACKEND = 'dogpile.cache.memory'
TIMEOUT = 10


def construct_cache(expiration_time=TIMEOUT):
    cache = make_region().configure(BACKEND, expiration_time=expiration_time)
    return cache


class CachedValue(object):
    def __init__(self, get_value_func, timeout=TIMEOUT):
        super(CachedValue, self).__init__()

        # 注意：这里调用 cache_on_arguments 其实返回了一个装饰器。
        self.cache = construct_cache(timeout)
        memoize = self.cache.cache_on_arguments()
        self.get_value = memoize(get_value_func)

    def get(self, key):
        return self.get_value(key)

    def __getitem__(self, key):
        return self.get_value(key)

    def __contains__(self, item):
        mapping = self.get_value()
        return mapping.__contains__(item)

    def __iter__(self):
        mapping = self.get_value()
        return iter(mapping)

import time
def get_time(id):
    return time.time() + int(id)


GET_TIME = CachedValue(get_time)


def test():
    import pdb; pdb.set_trace()
    while True:
        time.sleep(1)
        print(GET_TIME['0'])
        print(GET_TIME['1'])

if __name__ == '__main__':
    test()

