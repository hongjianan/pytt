# -*- coding: utf-8 -*-
'''
Created on 2018年5月9日

@author: Hong
'''

from time import sleep
from taskflow import task, engines
from taskflow.patterns import graph_flow
from taskflow.types import failure


class TaskA(task.Task):
    def execute(self, sleeptime, times, *args, **kwargs):
        print('T[%s] execute. sleeptime:%d times:%d args:%s kwargs:%s' %
            (self.__class__.__name__, sleeptime, times, args, kwargs))
        for i in range(times):
            print('round[%d]' % i)
            sleep(sleeptime)
        
    def revert(self, result, *args, **kwargs):
        print('T[%s] revert. result:%s args:%s kwargs:%s' %
            (self.__class__.__name__, result, args, kwargs))


class TaskB(task.Task):
    def execute(self, sleeptime, *args, **kwargs):
        print('T[%s] execute. sleeptime:%d args:%s kwargs:%s' %
            (self.__class__.__name__, sleeptime, args, kwargs))
        sleep(sleeptime)
        
    def revert(self, result, *args, **kwargs):
        print('T[%s] revert. result:%s args:%s kwargs:%s' %
            (self.__class__.__name__, result, args, kwargs))


class TaskC(task.Task):
    def execute(self, sleeptime, *args, **kwargs):
        print('T[%s] execute. sleeptime:%d args:%s kwargs:%s' %
            (self.__class__.__name__, sleeptime, args, kwargs))
        sleep(sleeptime)
        
    def revert(self, result, *args, **kwargs):
        print('T[%s] revert. result:%s args:%s kwargs:%s' %
            (self.__class__.__name__, result, args, kwargs))


def get_task_flow(sleeptime, times):
    flow = linear_flow.Flow('t1')
    flow.add(TaskA(),
             TaskB(),
             TaskC())
    
    store = {
        'sleeptime': sleeptime,
        'times': times,
    }
    
    return engines.load(flow, store=store)
    

def graph_tt():
    engine = get_task_flow(5, 2)
    engine.run()
    
        
if __name__ == '__main__':
    graph_tt()
    