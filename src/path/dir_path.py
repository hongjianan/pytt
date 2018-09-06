# -*- coding: utf-8 -*-
'''
Created on 2018年6月30日

@author: Administrator
'''
import os


def parse_path(path):
    dirname = os.path.dirname(path)
    filename = os.path.basename(path)
    print('dirname=%s, filename=%s' % (dirname, filename))
    
    new_path = os.path.join('/home/jason', filename)
    print('new_path=%s' % new_path)
    
if __name__ == '__main__':
    parse_path('/tmp/123.txt')
