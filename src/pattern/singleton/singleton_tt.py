# -*- coding: utf-8 -*-
'''
Created on 2018年6月12日

@author: Administrator
'''

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kw)  
        return cls._instance  


class System(Singleton):  
    def __init__(self):
        self.name = '123'
    
    def set_name(self, name):
        self.name = name

def new_tt():
    a = System()
    print(a.name)
    b = System()
    b.set_name('jason')
    print(a.name)

if __name__ == '__main__':
    new_tt()
