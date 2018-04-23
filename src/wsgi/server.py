# encoding: utf-8
'''
Created on 2018年4月11日

@author: Hong
'''

import os, sys
from copy import deepcopy
from wsgiref.util import application_uri


def run_with_cgi(application):
	environ = deepcopy(os.environ)
	environ['wsgi.input'] = sys.stdin
	environ['wsgi.error'] = sys.stderr
	environ['wsgi.version']      = (1, 0)
	environ['wsgi.multithread']  = False
	environ['wsgi.multiprocess'] = True
	environ['wsgi.run_once']     = True	        
	environ['wsgi.url_scheme'] = 'http'
    
	headers_set = []
	headers_send = []
    
	def write(data):
		sys.stdout.write(data)
		sys.stdout.flush()

	def start_response(status, response_headers, exc_info=None):
		headers_set[:] = [status, response_headers]
		return write
	
	result = application(environ, start_response)
	
	try:
		for data in result:
			if data:
				write(data)
	finally:
		if hasattr(result, 'close'):
			result.close()


if __name__ == '__main__':
	run_with_cgi(1)
	