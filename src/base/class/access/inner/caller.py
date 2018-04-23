# encoding: UTF-8
'''
Created on 2018年4月11日

@author: jason
'''

import provider

def access_tt():
    p = provider.Provider()
    p.public()
    p._package_public()
#     p.__private()    # access fail
    p.call__private()
    
    
if __name__ == '__main__':
    access_tt()
    