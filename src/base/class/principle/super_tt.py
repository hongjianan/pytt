# encoding: utf-8
'''
Created on 2018年4月29日

@author: Hong
'''

class A(object):
	def __init__(self):
		self.a = 'A'
	

class B(A):
	def __init__(self):
		super(B, self).__init__()
		self.b = 'B'


class C(B):
	def __init__(self):
		super(C, self).__init__()
		self.c = 'C'


def no_super_tt():
	c = C()
	print(c.c)
	print(c.b)
	print(c.a)


def super_tt():
	super(C, C()).
	pass

if __name__ == '__main__':
# 	no_super_tt()
	super_tt()
