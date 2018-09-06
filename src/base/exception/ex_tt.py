# -*- coding: utf-8 -*-
'''
Created on 2018年6月17日

@author: Administrator
'''

class ParamError(Exception):
    pass

def exception_tt():
    
    try:
        try:
            raise ParamError('parament error')
        except Exception as e:
            print(e)
            raise
    except ParamError as e:
        print(e)
    
if __name__ == '__main__':
    exception_tt()
    