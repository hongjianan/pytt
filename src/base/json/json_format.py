# -*- coding: utf-8 -*-
'''
Created on 2018年6月17日

@author: Administrator
'''
import json


def format_tt():
    person = {'name': 'jason', 'age': 10}
    jstr = json.dumps(person, sort_keys=True, indent=2, separators=(',', ': '))
    print(jstr)
    
    
if __name__ == '__main__':
    format_tt()
