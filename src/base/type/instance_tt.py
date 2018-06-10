# -*- coding: utf-8 -*-
'''
Created on 2018年6月1日

@author: Administrator
'''

class Animal(object):
    pass

class Lv(Animal):
    pass

class Horse(Animal):
    pass
    
class Luozi(Horse, Lv):
    pass
    
def isinstance_tt():
    luozi = Luozi()
    horse = Horse()
    print(isinstance(luozi, Lv), isinstance(horse, Lv))
    

if __name__ == '__main__':
    isinstance_tt()
    