# -*- coding: utf-8 -*-
'''
Created on 2018年8月4日

@author: Hong
'''

from time import sleep
from schedule import ITaskScheduler
from manager import RecoveryTaskManager
from assessor import RecoveryTaskAssessor
from task_api import ITask

from eventlet import greenpool
from eventlet import greenthread

        
class RecoveryTask(ITask):
    __task_type__ = 'planned_recover'

    def run(self, **kwargs):
        for i in range(1):
            print('RecoveryTask loop: %s run ...', i, self.get_cfg()['name'])
            greenthread.sleep(10)
        print('task end')
        

class NormalTask(ITask):
    __task_type__ = 'normal_task'

    def run(self, **kwargs):
        for i in range(2):
            pass
#             print('----NormalTask loop: %s run ...', i)
#             greenthread.sleep(10)
#         print('task end')
        

def run():

    ass = RecoveryTaskAssessor()
    manager = RecoveryTaskManager()
    scheduler = ITaskScheduler(manager, ass)
    scheduler.do_schedule()
    
#     task1 = RecoveryTask()
#     config = dict(name='task1', dst_cluster_id='100')
#     task1.set_cfg(config)
#     manager.add(task1, level=1)
#     
#     task2 = RecoveryTask()
#     config = dict(name='task2', dst_cluster_id='100')
#     task2.set_cfg(config)
#     manager.add(task2, level=2)
    
    sleep(10)
    for i in range(40000):
        if i == 20000:
            greenthread.sleep(10)
        n_task1 = NormalTask()
        manager.add(n_task1, level=1)
    
#     print(dir(scheduler.thread_pool))
#     
#     n_task1 = NormalTask()
#     manager.add(n_task1, level=1)
#     
#     print(scheduler.thread_pool.__dict__)
#     
#     n_task1 = NormalTask()
#     manager.add(n_task1, level=1)
#     
#     print(scheduler.thread_pool.__dict__)
    
    while True:
        greenthread.sleep(20)
        print(scheduler.thread_pool.__dict__)


if __name__ == '__main__':
    run()
