# -*- coding: utf-8 -*-
'''
Created on 2018年6月16日

@author: Administrator
'''

def switch_wrapper(fun):
    fun_name = fun.__name__
    def wrapper():
        ret = fun()
        print('test switch %s = %s' % (fun_name, ret))
    return wrapper


class TestSwitch():
    @staticmethod
    @switch_wrapper
    def test_you():
        return False

if __name__ == '__main__':
    TestSwitch.test_you()
