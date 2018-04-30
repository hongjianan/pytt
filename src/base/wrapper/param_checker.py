# -*- coding: utf-8 -*-
'''
Created on 2018年4月27日

@author: Hong
'''

import functools

def admin_checker(fun):
	@functools.wraps(fun)
	def _checker(*args, **kwargs):
		if kwargs.get('username') != 'admin':
			raise Exception('%s param username:%s is not admin' % (fun.__name__, kwargs.get('username')))
		return fun(*args, **kwargs)
		
	return _checker

class WSGI():
	
	@admin_checker
	def get_name(self, username):
		return 'admin'

def checker_tt():
	w = WSGI()
	print(WSGI.get_name.__name__)
	print(w.get_name(username='admin'))
	print(w.get_name(username='jason'))
	
	

if __name__ == '__main__':
	checker_tt()
