# -*- coding: utf-8 -*-
'''
Created on 2018年5月31日

@author: Administrator
'''
import sys
import inspect

def get_function_name():
    return inspect.stack()[1][3]

class A(object):
    def show(self):
        print('''
                 [CLASS:%s]
                 [FUNC:%s]
                 [FUNC:%s]
                 [FILE:%s]
                 [LINE:%s]''' % 
              (self.__class__.__name__,
               get_function_name(),
               sys._getframe().f_code.co_name,
               __file__,
               sys._getframe().f_lineno))

def show_code_info():
    a = A()
    a.show()
    
if __name__ == '__main__':
    show_code_info()
