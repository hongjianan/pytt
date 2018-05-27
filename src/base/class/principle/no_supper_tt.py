# -*- coding: utf-8 -*-
'''
Created on 2018年5月21日

@author: Administrator
'''

class A(object):
    VA = 'VA'
    def __init__(self):
        print('A __init__')
        self.a = 'A'
        

class B(A):
    VB = 'VB'
    def __init__(self):
        A.__init__(self)
        print('B __init__')
        self.b = 'B'


def no_supper_tt():
    b = B()
    print(b.a)
     
if __name__ == '__main__':
    no_supper_tt()
