# encoding: UTF-8
'''
Created on 2018年5月10日

@author: jason
'''


class A(object):
    def __init__(self):
        super(A, self).__init__()
        print('[A] __init__ class.name:%s' % self.__class__.__name__)


class B(object):
    def __init__(self):
        super(B, self).__init__()
        print('[B] __init__ class.name:%s' % self.__class__.__name__)

class C(A, B):
    pass
#     def __init__(self):
#         super(C, self).__init__()
#         B.__init__(self)
#         A.__init__(self)


def init_tt():
    C()
    
    
if __name__ == '__main__':
    init_tt()
