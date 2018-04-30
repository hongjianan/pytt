# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import ast

def parse_tt():
    print(ast.parse)
    p = ast.parse('x = 41')
    d = ast.dump(p)
    print(p)
    print(d)


if __name__ == '__main__':
    parse_tt()