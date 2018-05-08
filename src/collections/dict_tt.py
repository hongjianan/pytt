# -*- coding: utf-8 -*-
'''
Created on 2018年5月7日

@author: Administrator
'''
from collections import OrderedDict, defaultdict

def defaultdict_tt():
    

def ordereddict_tt():
    od = OrderedDict()
    od[1] = 'one'
    od[3] = 'three'
    od[2] = 'two'
    
    print(od)
    for k in od.keys():
        print(k, end='  ')
    print()
    
    d = {}
    d[4] = 'one'
    d[2] = 'three'
    d[3] = 'two'
    d[1] = 'two'
    for k in d.keys():
        print(k, end='  ')
    
if __name__ == '__main__':
    ordereddict_tt()
    