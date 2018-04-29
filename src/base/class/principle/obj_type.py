# encoding: utf-8
'''
Created on 2018年4月29日

@author: Hong
'''


def show_type():
	print('a'.__class__)	# str
	print('a'.__class__.__class__)	# type make str class
	
	
if __name__ == '__main__':
	show_type()
