# encoding: utf-8
'''
Created on 2018年4月23日

@author: Hong
'''

import __builtin__

class Tmp(object):
	def _tmp(self):
		print('this is _tmp')
	tmp = property(_tmp)
	
if __name__ == '__main__':
	t = Tmp()
	t.tmp
