# -*- coding: utf-8 -*-
'''
Created on 2018年4月22日

@author: Hong
'''

import inspect
class D:
    pass
 
class C(D):
    pass
 
class B(D):
    pass
 
class A(B, C):
    pass

class E(object):
	pass


if __name__ == '__main__':
	print inspect.getmro(D)
	print inspect.getmro(B)
	print inspect.getmro(C)
	print inspect.getmro(A)
	print(E.__mro__)