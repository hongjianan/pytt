# -*- coding: utf-8 -*-
'''
Created on 2018年6月3日

@author: Hong
'''

import web
  
urls = (  
    '/(.*)', 'hello'  
)  
  
app = web.application(urls, globals())  
  
class hello:  
    def GET(self, name):  
        i = web.input(times=1)  
        if not name:   
            name = 'world'  
        for c in xrange(int(i.times)):   
            print 'Hello,', name+'!'  
        return 'Hello, ' + name + '!'  
  
if __name__ == "__main__":  
    app.run()  
    