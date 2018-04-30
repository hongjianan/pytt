# -*- coding: utf-8 -*-
'''
Created on 2018年4月29日

@author: Hong
'''

import abc


class Person(object):
	__metaclass__ = abc.ABCMeta
	
	@abc.abstractmethod
	def say(self):
		''' '''

class Chinese(Person):
	def say(self):
		print('say Chinese')
		
	def eat(self):
		print('Chinese eat')
		

def abstract_tt():
# 	p = Person()
	c = Chinese()
	print(type(c))
	c.say()
	c.eat()

if __name__ == '__main__':
	abstract_tt()
	