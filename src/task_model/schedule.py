# coding=utf-8
# !/usr/bin/env python2
from datetime import datetime

from eventlet import greenpool
from eventlet import greenthread


class ITaskScheduler(object):
    def __init__(self, task_manager, task_assessor):
        self.time_delta = 4
        self.task_manager = task_manager
        self.task_assessor = task_assessor
        self.current_waiting_tasks = list()
        self.thread_pool = greenpool.GreenPool(2)
        

    def do_schedule(self):
        u"""
        进行调度执行任务
        """
        self.current_waiting_tasks = list()
        g = greenthread.spawn(self._schedule_run)
        return g

    def assessor_task(self, task):
        u"""
        评估任务是否可以执行
        :param task_id:
        :return:
        """
        running_tasks = self.task_manager.get_running_task()
        assess_result = self.task_assessor.assess(task, running_tasks)
        return assess_result

    def trim_tasks(self):
        u"""
        筛选出可执行的任务列表
        """
        wait_task_list = self.task_manager.list()
        wait_task_list.sort(key=lambda x: x.priority_level,
                            reverse=True)
        self.current_waiting_tasks = wait_task_list

    def exec_task(self):
        u"""
        依次执行任务
        """
        start_datetime = datetime.now()
        self.trim_tasks()
        runnable_task_list = self.current_waiting_tasks
        running_tasks = self.task_manager.get_running_task()
        
        # 将结束的任务从运行队列中剔除
        for task_id, task in running_tasks.items():
            if task.is_exit():
                self.task_assessor.remove_running_task(task)
                running_tasks.pop(task_id)
        
        # 将等待队列中任务，评估之后加入运行队列
        for task in runnable_task_list:
            if self.assessor_task(task):
                self.task_manager.run(self.thread_pool, task, start_datetime)
                self.task_assessor.add_running_task(task)
                self.task_manager.get_waiting_task().pop(task.id)

    def _schedule_run(self):
        while True:
            self.exec_task()
            greenthread.sleep(seconds=self.time_delta)
