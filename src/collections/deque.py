# -*- coding: utf-8 -*-
'''
Created on 2018年5月9日

@author: Hong
'''
from collections import deque

def deque_tt():
    nums = deque((1, 2, 3))
    print('origin', nums)
    
    print('pop', nums.pop())
    print('after pop', nums)

    print('popleft', nums.popleft())
    print('after popleft', nums)
    
    print('appendleft', nums.appendleft(1))
    print('after appendleft', nums)
    
    print('append', nums.append(3))
    print('after append', nums)

if __name__ == '__main__':
    deque_tt()
    