# -*- coding: utf-8 -*-
'''
Created on 2018年6月8日

@author: Administrator
'''

def dict2obj(d):  
    top = type('new', (object,), d)  
    seqs = (tuple, list, set, frozenset)
    for i, j in d.items():  
        if isinstance(j, dict):  
            setattr(top, i, dict2obj(j))  
        elif isinstance(j, seqs):  
            setattr(top, i,   
                type(j)(dict2obj(sj) if isinstance(sj, dict) else sj for sj in j))  
        else:  
            setattr(top, i, j)  
    return top  


def dict_to_obj():
    d = {'a': 1, 'b': {'c': 2}, 'd': ['hi', {'foo': 'bar'}]}
    obj = dict2obj(d)
    print(obj.a)
    print(obj.b.c)
    print(obj.d[0])
    print(obj.d[1].foo)


if __name__ == '__main__':
    dict_to_obj()
