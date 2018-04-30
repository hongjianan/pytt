# -*- coding: utf-8 -*-

import ctypes


def ctypes_tt():
    lib = ctypes.cdll.LoadLibrary("./libpycall.so")
    print(lib.foo(1, 3))


def run():
    ctypes_tt()


if __name__ == "__main__":
    run()
    

