# -*- coding: utf-8 -*-

# 动态参数 tuple *args   dict **kwargs
def show_tuple(*args):
    print(type(args), args)


def show_dict(**kwargs):
    print(type(kwargs), kwargs)


def show_any(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)


def show_anys(others, *args, **kwargs):
    print(others)
    print(type(args), args)
    print(type(kwargs), kwargs)


def func_attr():
    print(dir(len))
    print("__name__", len.__name__)


def dync_args():
    show_tuple(1, 2, 3)
    show_dict(k1 = 1, k2 = 2, k3 = 3)
    show_any(1, 2, 3, k1 = 1, k2 = 2, k3 = 3)
    show_any(0, 1, 2, 3, k1 = 1, k2 = 2, k3 = 3)

    l = [1, 2, 3]
    show_tuple(l)
    show_tuple(*l)

    d = {"name": "hong", "age": 20}
    show_dict(**d)


if __name__ == "__main__":
    func_attr()
    dync_args()
    
