# -*- coding: utf-8 -*-
'''
Created on 2018年5月8日

@author: Administrator
'''

import uuid

def uuid_tt():
    name = 'test'
    namespace = 'test_space'
    
    print(uuid.uuid1())
#     print(uuid.uuid3(namespace, name))
    print(uuid.uuid4())

if __name__ == '__main__':
    uuid_tt()
    