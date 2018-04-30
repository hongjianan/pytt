# -*- coding: utf-8 -*-
'''
Created on 2018年4月11日

@author: jason
'''

class Provider:
    def public(self):
        print('self.public')
        
    def _package_public(self):
        print('self._package_public')
        
    def __private(self):
        print('self.__private')
    
    def call__private(self):
        print('self.call__private')


def access_tt():
    p = Provider()
    p.public()
    p._package_public()
#     p.__private()    # access fail
    p.call__private()


if __name__ == '__main__':
    access_tt()
    