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
    def __init__(self):
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


class B(A):
    pass


def show_code_info():
#     A()
    B()
    
if __name__ == '__main__':
    show_code_info()
