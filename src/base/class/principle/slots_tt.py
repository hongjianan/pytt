# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('name:%s' % self.name)
    
class Person2(object):
    __slots__ = 'name'
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ('name:%s' % self.name)
        

@profile
def slots_tt():
    ps = [Person('jason') for i in range(1000)]
    ps2 = [Person2('jason') for i in range(1000)]
    
    
if __name__ == '__main__':
    slots_tt()
    