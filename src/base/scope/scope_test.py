# -*- coding: utf-8 -*-

'''
1. python 没有块作用域的概念，
2. 数未执行之前，作用域已经形成了，作用域链也生成了
'''

NAME = "hong"


def func1():
    global NAME
    print(NAME)

    name = "hjn"
    NAME = "nan"
    print(name, NAME)


def func2():
    print(NAME)


def lambda_tt():
    l = [lambda : x for x in range(10)]
    print(l[0]())
    
    def fun_ret(x):
        return x
    
    l = []
    for i in range(10):
        l.append(fun_ret(i))
    print(l[0])
    
if __name__ == "__main__":
#     func1()
#     func2()
    lambda_tt()
    

