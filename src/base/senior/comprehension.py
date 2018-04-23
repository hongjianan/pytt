# encoding: UTF-8
'''
Created on 2018年4月23日

@author: jason
'''

'''
variable = [out_exp_res for out_exp in input_list if out_exp == 2]
    out_exp_res:　　列表生成元素表达式，可以是有返回值的函数。
    for out_exp in input_list：　　迭代input_list将out_exp传入out_exp_res表达式中。
    if out_exp == 2：　　根据条件过滤哪些值可以。
'''
def list_comprehension_1():
    # no use comprehension
    l = []
    for i in range(10):
        if (i % 2 == 0):
            i = i * i
            l.append(i)
    print(l)
    
    # equal to
    l = [(i*i) for i in range(10) if (i % 2 == 0)]
    print(type(l))
    print(l)
    
    # function 
    def square(i):
        return i * i
    l = [square(i) for i in range(10) if (i % 2 == 0)]
    print(l)
    
    # 不能使用 lambda，会直接返回 lambda表达式
    l = [lambda i: i*i for i in range(10) if (i % 2 == 0)]
    print(l)


def set_comprehension_1():
    s = {(i*i) for i in range(10) if (i % 2 == 0)}
    print(type(s))
    print(s)
        
        
def generator_comprehension_1():
    gen = ((i*i) for i in range(10) if (i % 2 == 0))
    print(type(gen))
    for i in gen:
        print(i)


def dict_comprehension_1():
    d = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
    dc = {
        k.lower(): d.get(k.lower(), 0) + d.get(k.upper(), 0)
        for k in d.keys()
        if k.lower() in ['a','b']
    }
    print(dc)
    
    
def dict_comprehension_2():
    d = {'one': 1, 'two': 2}
    dc = {
        v:k 
        for k,v in d.items()
    }
    print(dc)


if __name__ == '__main__':
#     list_comprehension_1()
    set_comprehension_1()
#     generator_comprehension_1()
#     dict_comprehension_1()
#     dict_comprehension_2()

