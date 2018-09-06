# -*- coding: utf-8 -*-
'''
Created on 2018年6月30日

@author: Administrator
'''
import six
import functools

def wrapper(func):
#     print('wrapper1')
    @six.wraps(func)
    def _wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return _wrapper


def recover_name(name):
    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return __wrapper
    _wrapper.__name__ = name
    return _wrapper


class Dog(object):
    def __init__(self):
        self.name = 'Dog'
    
    @wrapper
    def bak(self):
        print('Dog bak', self.name)
    
    @wrapper
    def eat(self):
        print('Dog eat', self.name)


class Cat(object):
    def __init__(self):
        self.name = 'Cat'
    
#     @wrapper
#     def bak(self):
#         print('Cat miao', self.name)

    @wrapper
    def miao(self):
        print('Cat miao', self.name)

        
class Facade(object):
    def __init__(self, subsystem_list):
        self.__subsystems = subsystem_list
        self.__register_interface()

    def __register_interface(self):
        interfaces = set()

        for subsystem in self.__subsystems:
            attrs = dir(subsystem)
            for attr in attrs:
                if attr.startswith('_'):
                    continue
    
                attr_obj = getattr(subsystem, attr)
                if hasattr(attr_obj, '__call__'):
                    print(attr, attr_obj)
                    assert(attr not in interfaces)
                    interfaces.add(attr)
                    setattr(self, attr, attr_obj)


class AnimalFaker(Facade):
    def __init__(self):
        controllers = list()
        controllers.append(Dog())
        controllers.append(Cat())

        super(AnimalFaker, self).__init__(controllers)
        
    
def attr_tt():
    faker = AnimalFaker()

    print(dir(faker))
    faker.bak()
    faker.eat()
    faker.miao()

if __name__ == '__main__':
    attr_tt()
