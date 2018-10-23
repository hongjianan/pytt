# -*- coding: utf-8 -*-
'''
Created on 2018年10月23日

@author: Administrator
'''

import tools
from tools import hmath

def package_tt():
    print(tools.hadd(2, 1))
    print(hmath.hadd(2, 1))
    print(hmath.hsub(2, 1))

if __name__ == '__main__':
    package_tt()
