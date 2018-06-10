# -*- coding: utf-8 -*-
'''
Created on 2018年5月28日

@author: Administrator
'''

class ULog(object):
    def __init__(self, id=None, size=None):
        self.params = locals().copy()
        print(self.params)
        
    def __enter__(self):
        # 使用已有的日志初始化关系
        id = self.params.pop('id', None)
        print('__enter__, id', id)
        return self

    def __exit__(self, type, value, trace):
        pass


def locals_tt1():
    with ULog(1, 10) as ulog_1:
        with ULog(2, 20) as ulog_2:
            pass

def locals_tt2():
    with ULog() as ulog_1:
        with ULog() as ulog_2:
            pass   


def locals_tt(a, b, c, *args, **kwargs):
    loc = locals()
    print(loc)


if __name__ == '__main__':
#     locals_tt1()
#     locals_tt2()
    locals_tt(1, 2, 3, 4, name='jason')
    