# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

name = 0

def f1():
    name = 1
    def f2():
        name = 2
        print('f2', name)
    print('f1', name)
    f2()
    print('f1', name)


def func_link():
    f1()
    print(name)


if __name__ == '__main__':
    func_link()
    