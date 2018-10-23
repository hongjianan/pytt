# -*- coding: utf-8 -*-
'''
Created on 2018年4月29日

@author: Hong
'''

class ObjectCreator(object):
    pass

class Apple(object):
    pass

class Orange(object):
    pass

def showobj(obj):
    print(obj)
    print(hasattr(obj, 'name'), obj.name)
    print(obj.__dict__)

def addattr():
    ObjectCreator.name = 'creator'

def choose_class(cls):
    if cls == 'apple':
        return Apple
    elif cls == 'orange':
        return Orange
    return None


def addattr_tt():
    addattr()
    showobj(ObjectCreator)


def choose_tt():
    cls = choose_class('apple')
    print(type(cls), cls)
    apple = cls()
    print(apple)


def create_tt():
    Car = type('Car', (), {})
    print(type(Car), Car)
    
    Animal = type('Animal', (), {'count': 0})
    Person = type('Person', (Animal,), {'name': 'Person'})
    print(Person.name)
    p = Person()
    
    
    
if __name__ == '__main__':
#     addattr_tt()
#     choose_tt()
    create_tt()
    