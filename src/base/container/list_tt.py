# -*- coding: utf-8 -*-
'''
Created on 2018年5月30日

@author: Administrator
'''


def list_tt():
    l = [0, 1, 2, 3, 4, 5]
    print(l)
    
    for i in reversed(l):
        print(i)
        
    # reverse
    lr1 = list(reversed(l))
    print(lr1)
    
    lr2 = l[::-1]
    print(lr2)
    
    lr3=sorted(l, cmp=None, key=None, reverse=True)
    print(lr3)


if __name__ == '__main__':
    list_tt()
    