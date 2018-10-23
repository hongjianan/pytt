# -*- coding: utf-8 -*-
'''
Created on 2018年8月6日

@author: Hong
'''
import time
from expiredict import ExpireDict


def dict_tt():
    expd = ExpireDict(3)
    expd[1] = '11'
    expd[2] = '22'
    expd[3] = '33'
    expd[4] = '44'
    print('..', expd.get(1, None))
    expd.set_ttl(4, 2)
    print(expd)
    time.sleep(4)
    print(expd)
#     print(expd[1])
    print(expd[2])
    
if __name__ == '__main__':
    dict_tt()
