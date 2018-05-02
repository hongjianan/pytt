# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import collections

def no_collections_tt():
    def add_family(collect, person, family):
        if family not in collect:
            collect[family] = set()
        collect[family].add(person)
    
    all = {}
    add_family(all, 'jason', 'hong')
    add_family(all, 'jianan', 'hong')
    add_family(all, 'xiao', 'li')
    for k, v in all.items():
        print(k, v)
        

def defaultdict_tt():
    def add_family(collect, person, family):
        collect[family].add(person)
        
    all = collections.defaultdict(set)
    add_family(all, 'jason', 'hong')
    add_family(all, 'jianan', 'hong')
    add_family(all, 'xiao', 'li')
    
    for k, v in all.items():
        print(k, v)
    
    print(dir(all))
    
    
if __name__ == '__main__':
    no_collections_tt()
#     defaultdict_tt()
    