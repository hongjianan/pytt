# -*- coding: utf-8 -*-
'''
Created on 2018年4月29日

@author: Hong
'''

class A(object):
	VA = 'VA'
	def __init__(self):
		self.a = 'A'
	

class B(A):
	VB = 'VB'
	def __init__(self):
		super(B, self).__init__()
		self.b = 'B'


class C(B):
	VC = 'VC'
	def __init__(self):
		super(C, self).__init__()
		self.c = 'C'


def class_super_tt():
	c = C()
	print(c.c)
	print(c.b)
	print(c.a)


def super_tt():
	print(super(C, C()).VB)
	

if __name__ == '__main__':
# 	class_super_tt()
	super_tt()
