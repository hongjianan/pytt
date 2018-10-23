# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: Hong
'''
import unittest

class TestFail(unittest.TestCase):
    
    def test_range(self):
        for x in range(3):
            if x > 2:
                self.fail('range over 2')
    
    @unittest.skip('Do not run this')
    def test_fail(self):
        self.fail('test fail')
    
    @unittest.skipIf('Do not run this')
    def test_fail(self):
        self.fail('test fail')
        
    @unittest.skip('Do not run this')
    def test_success(self):
        self.assertEqual(1, 1)
        

class TestMe(unittest.TestCase):


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()