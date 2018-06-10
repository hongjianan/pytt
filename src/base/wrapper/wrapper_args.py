# -*- coding: utf-8 -*-

import functools

USER_NAME = "jason"
USER_AGE = 27


def result_wrapper(times):
    def caller(func):
        @functools.wraps(func)
        def args(*args, **kwargs):
            result = func(*args, **kwargs)
            return times * result
        return args
    return caller


def times_wrapper(times, func):
    def args(*args, **kwargs):
        result = func(*args, **kwargs)
        return times * result
    return args

@result_wrapper(10)
def add(a, b):
    return a + b

def sub(a, b):
    return a - b


def args_tt():
    print(add(1, 2))
    print(times_wrapper(20, sub)(3, 1))
    

if __name__ == "__main__":
    args_tt()
