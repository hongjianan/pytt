# -*- coding: utf-8 -*-
'''
Created on 2018年5月7日

@author: Administrator
'''
from collections import Counter

def counter_tt():
    ret = Counter('aabbcc')
    print(type(ret))
    print(dir(ret))
    print(ret.__dict__, ret)
    
    # top n
    cnt = Counter([1, 1, 1, 2, 2, 3])
    print(cnt.most_common(2))
    

if __name__ == '__main__':
    counter_tt()
    