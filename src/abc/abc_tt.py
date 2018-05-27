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
	
	@abc.abstractmethod
	def name(self):
		''' '''	
	

class Chinese(Person):
	def __init__(self, name):
		self._name = name
	
	def say(self):
		print('say Chinese')
		
	def eat(self):
		print('Chinese eat')
	
	@property
	def name(self):
		return self._name
		

def abstract_tt():
# 	p = Person()
	c = Chinese('jason')
	print(type(c))
	c.say()
	c.eat()
	print(c.name())

if __name__ == '__main__':
	abstract_tt()
	