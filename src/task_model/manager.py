# coding=utf-8
# !/usr/bin/env python2
from datetime import datetime, timedelta

from task_api import WAITING, RUNNING, CANCELLED


class ITaskManager(object):
    def __init__(self):
        self.waiting_task = dict()
        self.running_task_list = list()

    def add(self, task, **kwargs):
        u"""
        装填任务
        :param task: 任务实例
        :param kwargs: priority_level = priority_level
                       deadline = deadline
                       timeout_cancel = timeout_cancel
        :return: task.id
        """
        deadline = kwargs.get('deadline', datetime.now() + timedelta(hours=5))
        timeout_cancel = kwargs.get('timeout_cancel', False)
        priority_level = kwargs.get('level', 0)
        task.priority_level = priority_level
        task.deadline = deadline
        task.timeout_cancel = timeout_cancel
        self.waiting_task[task.task_id] = task
        return task.task_id

    def delete(self, task_id):
        u"""
        删除任务
        :param task_id:
        """
        task = self.waiting_task.get(task_id)
        if task:
            if task.task_status == RUNNING and task in self.running_task_list:
                task.task_cancelled()
                self.running_task_list.remove(task)
            self.waiting_task.pop(task_id)

    def list(self):
        u"""
        列出所装填的所有任务
        :return: list(task....) 任务列表
        """
        return self.waiting_task.values()

    def status(self, task_id):
        u"""
        查看当前任务状态
        :param task_id: 任务id
        :return: task的状态
        """
        task = self.waiting_task.get(task_id)
        return task.task_status

    def set_priority(self, task_id, priority):
        u"""
        设置任务的权重
        :param task_id: 任务id
        :param priority: 权重(int)
        """
        task = self.waiting_task.get(task_id)
        if task:
            task.priority_level = priority

    def get_priority(self, task_id):
        u"""
        获取任务的权重
        :param task_id: 任务id
        :return: 任务村存在且
        """
        task = self.waiting_task.get(task_id)
        if task:
            priority = task.priority_level
            return priority

    def run(self, thread_pool, task_id, start_point):
        u"""
        运行任务
        :param thread_pool: 协程池
        :param task_id: 任务id
        :param start_point: 调度开始时间
        """
        task = self.waiting_task.get(task_id)
        if task:
            if task.task_status == WAITING:
                if task.timeout_cancel and task.deadline:
                    schedule_time = (start_point - datetime.now()).seconds
                    if schedule_time > task.deadline:
                        task.task_status = CANCELLED
                        self.delete(task_id)
                        return
                task.task_status = RUNNING
                self.running_task_list.append(task)
                thread_pool.spawn_n(task.run)


class RecoveryTaskManager(ITaskManager):
    

    def __init__(self):
        self.waiting_task = dict()
        self.running_task = dict()

    def add(self, task, **kwargs):
        u"""
        装填任务
        :param task: 任务实例
        :param kwargs: priority_level = priority_level
                       deadline = deadline
                       timeout_cancel = timeout_cancel
        :return: task.id
        """
#         print('add task: %s', task)
        deadline = kwargs.get('deadline', datetime.now() + timedelta(hours=5))
        timeout_cancel = kwargs.get('timeout_cancel', False)
        priority_level = kwargs.get('level', 0)
        task.priority_level = priority_level
        task.deadline = deadline
        task.timeout_cancel = timeout_cancel
        self.waiting_task[task.id] = task
        return task.id

    def delete(self, task):
        u"""
        删除任务
        :param task:
        """
        if task:
            if task.task_status == RUNNING and task.id in self.running_task:
                task.task_cancelled()
                self.running_task.pop(task.id)
            else:
                self.waiting_task.pop(task.id)

    def list(self):
        u"""
        列出所装填的所有任务
        :return: list(task....) 任务列表
        """
        return self.waiting_task.values()

    def status(self, task_id):
        u"""
        查看当前任务状态
        :param task_id: 任务id
        :return: task的状态
        """
        task = self.waiting_task.get(task_id)
        return task.task_status

    def set_priority(self, task_id, priority):
        u"""
        设置任务的权重
        :param task_id: 任务id
        :param priority: 权重(int)
        """
        task = self.waiting_task.get(task_id)
        if task:
            task.priority_level = priority

    def get_priority(self, task_id):
        u"""
        获取任务的权重
        :param task_id: 任务id
        :return: 任务村存在且
        """
        task = self.waiting_task.get(task_id)
        if task:
            priority = task.priority_level
            return priority
        
    def get_running_task(self):
        return self.running_task
    
    def get_waiting_task(self):
        return self.waiting_task

    def run(self, thread_pool, task, start_point):
        u"""
        运行任务
        :param thread_pool: 协程池
        :param task_id: 任务id
        :param start_point: 调度开始时间
        """
        if task:
            if task.task_status == WAITING:
                if task.timeout_cancel and task.deadline:
                    schedule_time = (start_point - datetime.now()).seconds
                    if schedule_time > task.deadline:
                        task.task_status = CANCELLED
                        self.delete(task)
                        return
                task.task_status = RUNNING
                self.running_task[task.id] = task
                thread_pool.spawn_n(task.catch_run)
