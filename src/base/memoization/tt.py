# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import math

_SIN_MEMORY = {}

def mem_sin(x):
    if x not in _SIN_MEMORY:
        result = math.sin(x)
        _SIN_MEMORY[x] = result
    return result


def tt():
    print(mem_sin(10))

if __name__ == '__main__':
    tt()
    