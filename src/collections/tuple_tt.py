# -*- coding: utf-8 -*-
'''
Created on 2018年5月7日

@author: Administrator
'''

from collections import namedtuple

def namedtuple_tt():
    point = namedtuple('point3', ['x', 'y', 'z'])
    a = point(1, 2, 3)
    print(a)
    print(a.x, a.y, a.z)
    
if __name__ == '__main__':
    namedtuple_tt()
    
    