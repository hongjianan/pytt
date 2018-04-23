# encoding: utf-8
'''
Created on 2018年4月10日

@author: Hong
'''

class Person:
	desc = 'person'
	def __init__(self, name, age):
		self.name = name
		self.age = age
	

def obj_member_tt():
	p = Person('jason', 18)
	print('obj', p.__dict__)
	
	print('class', Person.__dict__)
	
	
if __name__ == '__main__':
	obj_member_tt()
	