# -*- coding: utf-8 -*-
'''
Created on 2018年4月28日

@author: Hong
'''

from enum import (
	Enum,
# 	unique
)

# @unique # if wrapper unique, red_alis != 1
class Color(Enum):
	red = 1
	yellow = 2
	blue = 3
	red_alis = 1
	
	
def enum_tt():
	print(type(Color.red))
	
	print(Color.red)
	print(Color(1))
	print(Color['red'])
	print(Color.red.name)
	print(Color.red.value)
	
	if Color.red == Color.red_alis:
		print('Color.red == Color.red_alis')
	else:
		print('Color.red != Color.red_alis')
		
	for i in Color:
		print(i, i.value)
		
	print(type(Color.__members__))
	for k, v in Color.__members__.items():
		print(k)
		print(v)

def use_tt():
	light = Color.red
	print('light is red', light == Color.red)
	
if __name__ == '__main__':
# 	enum_tt()
	use_tt()
	