# -*- coding: utf-8 -*-
'''
Created on 2018年4月28日

@author: Administrator
'''

from enum import Enum

# !!!!!!!!!这么用Enum是不行的， class中的成员是不能修改的
class Light(Enum):

    CLOSE = 2
    OPEN = 1
    
    def __init__(self):
        self._status = Light.CLOSE
        
    @property
    def status(self):
        return self._status
        
    @status.setter
    def status(self, status):
        self._status = status
        
    def open(self):
        self.status = Light.OPEN
    
    def close(self):
        self.status = Light.CLOSE
        
def light_tt():
    l = Light()
    l.open()
    print(l.status)
    
    l.close()
    print(l.status)
    
if __name__ == '__main__':
    light_tt()
    