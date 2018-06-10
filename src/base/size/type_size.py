# -*- coding: utf-8 -*-
'''
Created on 2018年5月30日

@author: Administrator
'''

from sys import getsizeof
   
class A(object):
    pass

class B:
    pass

class Counter(object):
    def __init__(self, count=0):
        self.count = count


def type_size():
    for x in (None, 1, 1L, 1.2, 'c', [], [1], (), {}, set(), B, B(), A, A(), Counter, Counter()):
        print "{0:20s}\t{1:d}".format(type(x).__name__, getsizeof(x))


if __name__ == '__main__':
    type_size()
    