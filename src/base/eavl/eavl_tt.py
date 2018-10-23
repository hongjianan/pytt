# -*- coding: utf-8 -*-
'''
Created on 2018年10月23日

@author: Administrator
'''

def test_first():
    return 3

def test_second(num):
    return num

action = {  # 可以看做是一个sandbox
    "para": 5,
    "test_first" : test_first,
    "test_second": test_second
}

def eavl_tt():  
    condition = "para == 5 and test_second(test_first) > 5"
    res = eval(condition, action)  # 解释condition并根据action对应的动作执行
    print res

if __name__ == '__main__':
    eavl_tt()
