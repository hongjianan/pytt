# -*- coding: utf-8 -*-
'''
Created on 2018年5月7日

@author: Administrator
'''
from collections import OrderedDict, defaultdict

def defaultdict_tt():
    colors = ['red', 'green', 'red']
    
    # method 1
    count = {}
    for color in colors:
        if color not in count:
            count[color] = 1
        else:
            count[color] += 1
    print(count)
    
    # method 2
    count = {}
    for color in colors:
        count.setdefault(color, 0)
        count[color] += 1
    print(count)
    
    # method 3
    count = defaultdict(int)
    for color in colors:
        count[color] += 1
    print(count)
    
    # multiple dict
    def gen_default():
        return {'name': 'jason', 'age': 0}
    users = defaultdict(gen_default)    # gen_default 为可调用对象
    
    users['jason']['age'] += 10
    print(users['jason'])


def ordereddict_tt():
    # ordered dict
    od = OrderedDict().
    od[1] = 'one'
    od[3] = 'three'
    od[2] = 'two'
    print(od)
    print(od.popitem())
    
    # normal dict
    d = {}
    d[1] = 'one'
    d[3] = 'three'
    d[2] = 'two'
    print(d)
    
if __name__ == '__main__':
#     defaultdict_tt()
    ordereddict_tt()
    