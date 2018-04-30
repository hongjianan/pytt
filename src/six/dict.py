# -*- coding: utf-8 -*-
'''
Created on 2018年4月30日

@author: Administrator
'''

import six

def iteritems_tt():
    d = {1: 'one', 2: 'two',}
    for k, v in d.items():
        print(k, v)
    
    for k, v in six.iteritems(d):
        print(k, v)
'''
    # python3 dict has no iteritems
    for k, v in d.iteritems():
        print(k, v)
'''    
if __name__ == '__main__':
    iteritems_tt()
    