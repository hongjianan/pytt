# -*- coding: utf-8 -*-
'''
Created on 2018年5月3日

@author: Administrator
'''

class Animal(object):
    name = 'Base'
    def __init__(self):
        super(Animal, self).__init__()
    
class Dog(Animal):
    name = 'Dog'
    def __init__(self):
        super(Animal, self).__init__()

def classmember_tt():
    d = Dog()
    print(d.name, Dog.name)
    
if __name__ == '__main__':
    classmember_tt()
    