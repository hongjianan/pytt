'''
Created on 2018-4-9

@author: jason
'''
from .matherror import MathError

def add(a, b):
    raise MathError('jj')
    return a + b

def sub(a, b):
    return a - b

if __name__ == '__main__':
    pass