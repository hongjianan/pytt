# -*- coding: utf-8 -*-
'''
Created on 2018年4月26日

@author: Hong
'''
import unittest

import os
cur_dir = os.path.basename(__file__)
src_dir = os.path.join(cur_dir, '../../src')

import sys
sys.path.append(src_dir)
from common import hmath

class TestHmath(unittest.TestCase):

        
    def test_add(self):
        self.assertEqual(3, hmath.add(1, 2))
        self.assertNotEqual(0, hmath.add(0, 1))
        
    def test_div(self):
        """Test Hmath div(a, b)"""
        self.assertEqual(2.5, hmath.div(5, 2))
        pass
    
    def test_last(self):
        print('======test_last========')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestHmath.test_dir']
    unittest.main(verbosity=2)