# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import ast

hello_world = ast.Str(s='hello world', lineno=1, col_offset=1)
print_call = ast.Print(values=[hello_world], lineno=1, col_offset=1, nl=True)
module = ast.Module(body=[print_call])
code = compile(module, '', 'exec')
eval(code) 

if __name__ == '__main__':
    pass