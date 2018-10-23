# -*- coding: utf-8 -*-
'''
Created on 2018年5月3日

@author: Administrator
'''

import const

class LockType(object):
    const.LOCK = 'L'
    const.UNLOCK = 'U'
    
    @classmethod
    def values(cls):
        return (const.LOCK, const.UNLOCK)

def define_const():
#     const.a = 'a'
    const.A = 'a'
    print(const.A)


def const_class():
    print(type(const.LOCK), const.LOCK)
    print(LockType.values())


if __name__ == '__main__':
    define_const()
    const_class()
    