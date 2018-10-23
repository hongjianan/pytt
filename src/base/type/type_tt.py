# -*- coding: utf-8 -*-
'''
Created on 2018年7月3日

@author: Hong
'''

def create_obj():
    Person = type('Person', (object,), {'count': 0})
    p1 = Person()
    print(p1.__dict__)
    print(dir(p1))

if __name__ == '__main__':
    create_obj()
