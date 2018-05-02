# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import sys

class Null:
    pass

class Person1:
    def __init__(self, age):
        self.age = age
        
class Person2(object):
    def __init__(self, age):
        self.age = age
        
class Person3(object):
    __slot__ = 'age'
    def __init__(self, age):
        self.age = age


def sizeof_tt():
    print('int', sys.getsizeof(int))
    print('boolean', sys.getsizeof(True))
    print('Null', sys.getsizeof(Null))
    print('Person1', sys.getsizeof(Person1))
    print('Person2', sys.getsizeof(Person2))
    print('Person3', sys.getsizeof(Person3))
    
    print('Person2 obj', sys.getsizeof(Person2(2)))
    print('Person3 obj', sys.getsizeof(Person3(3)))
    
    
if __name__ == '__main__':
    sizeof_tt()
