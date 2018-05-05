# -*- coding: utf-8 -*-
'''
Created on 2018年5月4日

@author: Administrator
'''

from taskflow.types import failure
from taskflow import task, retry, engines
from taskflow.patterns import linear_flow

ga = 0
gb = 0
gc = 0

class RevertingTask(task.Task):
    def execute(self, *args, **kwargs):
        print('start RevertingTask')
        raise Exception('123')
        
#     def revert(self, result, flow_failures):
#         if isinstance(result, failure.Failure):
#             print('revert result is failure', result)
#         else:
#             print('revert result is not failure', result)
        

def revert_tt():
    flow = linear_flow.Flow('f1')
    flow.add(RevertingTask())
    engines.run(flow)
    
    
if __name__ == '__main__':
    revert_tt()
    