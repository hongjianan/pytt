# -*- coding: utf-8 -*-
'''
Created on 2018年5月3日

@author: Administrator
'''

class Animal(object):
    name = 'Base'
    def __init__(self):
        super(Animal, self).__init__()
    
    def eat(self):
        print('Animal eat')
        
    def sleep(self):
        print('Animal sleep')
            
    def show(self):
        self.eat()
        self.sleep()
    
class Dog(Animal):
    name = 'Dog'
    def __init__(self):
        super(Animal, self).__init__()
    
    def eat(self):
        print('Dog eat')


def dync_tt():
    dog = Dog()
    dog.show()
    
        
def classmember_tt():
    d = Dog()
    print(d.name, Dog.name)
    
if __name__ == '__main__':
#     classmember_tt()
    dync_tt()
