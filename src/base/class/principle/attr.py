# -*- coding: utf-8 -*-
'''
Created on 2018年5月3日

@author: Administrator
'''

class StaticTest:
    
#     kv = StaticTest.__get_dict()
#     
#     @staticmethod
#     def __get_dict():
#         k0 = (False, False)
#         k1 = (False, True)
#         k2 = (True, False)
#         k3 = (True, True)
#         v0 = 0
#         v1 = 1
#         v2 = 2
#         v3 = 3
#         return {k0: v0,
#                 k1: v1,
#                 k2: v2,
#                 k3: v3}
    
    kv = {(False, False): 0, (False, True): 1, (True, False): 2, (True, True): 3}
    
    def __init__(self, x, y):
        self.value = StaticTest.kv[(x, y)]
        
    def get_value(self):
        return self.value
    

class Person():
    pass


def attr_tt():
    s = StaticTest(False, True)
    print(s.get_value())
    

if __name__ == '__main__':
    attr_tt()
    