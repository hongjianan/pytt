# -*- coding: utf-8 -*-
'''
Created on 2018年8月7日

@author: Hong
'''

from eventlet import greenpool
from eventlet import greenthread

count = 0

def func():
    global count
    count += 1
    idx = count
    print('%s start' % idx)
    greenthread.sleep(10)
    print('%s end' % idx)
    
    
def gthread():
    pool = greenpool.GreenPool(2)
    pool.spawn_n(func)
    pool.spawn_n(func)
    pool.spawn_n(func)
    
    while True:
        greenthread.sleep(10)
    
if __name__ == '__main__':
    gthread()
