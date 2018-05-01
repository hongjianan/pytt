# -*- coding: utf-8 -*-
'''
Created on 2018年5月1日

@author: Hong
'''

import mock

def mock_tt():
	m = mock.Mock()
	m.some_method.return_value = 1
	print(m.some_method())

if __name__ == '__main__':
	mock_tt()