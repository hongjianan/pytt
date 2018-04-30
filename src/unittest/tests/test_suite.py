# -*- coding: utf-8 -*-
'''
Created on 2018年4月26日

@author: Hong
'''
import unittest

from test_common.test_hmath import TestHmath


if __name__ == "__main__":
	suite = unittest.TestSuite()
	tests = [TestHmath('test_add'), TestHmath('test_div')]
	suite.addTests(unittest.TestLoader().loadTestsFromNames(['TestHmath']))
	suite.addTests(tests)
	
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suite)
	
	'''
	# 直接用addTest方法添加单个TestCase
suite.addTest(TestMathFunc("test_multi"))

# 用addTests + TestLoader
# loadTestsFromName()，传入'模块名.TestCase名'
suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc.TestMathFunc'))
suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc.TestMathFunc']))  # loadTestsFromNames()，类似，传入列表

# loadTestsFromTestCase()，传入TestCase
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
	'''
