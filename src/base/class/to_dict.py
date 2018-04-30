# -*- coding: utf-8 -*-


class Person:
    desc = 'Person'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


def object_member_tt():
    p = Person('hong', 18)
    pd = p.__dict__
    print(pd)

def class_member_tt():
    p = Person('jason', 18)
    [name for name in dir(p) if not name.startswith('__')]
    print('Person class member', name)
    pd = dict((name, getattr(p, name)) for name in dir(p) if not name.startswith('__'))
    print(pd)   
    

if __name__ == '__main__':
    object_member_tt()
    class_member_tt()
    