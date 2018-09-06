# -*- coding: utf-8 -*-
'''
Created on 2018年6月29日

@author: Administrator
'''

class BaseA(object):
    def __init__(self):
        self.name = 'BaseA'
        
    def show(self):
        print('self.name', self.name)


class BaseB(object):
    def __init__(self):
        self.name = 'BaseB'
        
    def show(self):
        print('self.name', self.name)

        
class C(BaseA, BaseB):
    pass


def class_112_tt():
    c = C()
    c.show()


if __name__ == '__main__':
    class_112_tt()
