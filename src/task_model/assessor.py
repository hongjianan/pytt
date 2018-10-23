# coding=utf-8
# !/usr/bin/env python2


class ITaskAssessor(object):
    def assess(self, task, running_tasks):
        raise NotImplementedError


PLANNED_RECOVER_TASK_TYPE = 'planned_recover'
DISASTER_RECOVER_TASK_TYPE = 'disaster_recover'


import collections
# from oslo_log import log
# 
# LOG = log.getLogger(__name__)


class RecoveryTaskAssessor(ITaskAssessor):
    u""" 恢复任务调度评估  """
    CONFIG = {
        "src_cluster_id": 123,
        "dst_cluster_id": 123,
    }
    cluster_recy_tasks = collections.defaultdict(int)

    RECOVERY_TASK_TYPE = (PLANNED_RECOVER_TASK_TYPE,
                          DISASTER_RECOVER_TASK_TYPE)

    def get_task_dst_cluster_id(self, task):
        return task.get_cfg()['dst_cluster_id']

    def is_recovery_task(self, task):
        u""" 是否是恢复任务 """
        if task.get_type() in self.RECOVERY_TASK_TYPE:
            return True
        return False

    def assess(self, task, running_tasks):
#         import pdb
#         pdb.set_trace()
        if not self.is_recovery_task(task):
            return True
        dst_cluster_id = self.get_task_dst_cluster_id(task)

        # 目的站点的恢复任务大于限制
        if self.cluster_recy_tasks[dst_cluster_id] >= \
                self.get_cluster_task_limit(dst_cluster_id):
            print('recovery task: %s can not add to running task',
                      task.id)
            return False
        return True

    def get_cluster_task_limit(self, cluster_id):
        return 1
#         return self.get_cluster_hosts(cluster_id) * 2

    def get_cluster_hosts(self, cluster_id):
        return 0

    def remove_running_task(self, task):
        if not self.is_recovery_task(task):
            return
        
        print('remove_running_task task:%s ', task.get_cfg()['name'])
        dst_cluster_id = self.get_task_dst_cluster_id(task)
        if self.cluster_recy_tasks[dst_cluster_id] <= 0:
            print('dst_cluster_id: %s task count: %s can not < 0',
                      dst_cluster_id, self.cluster_recy_tasks[dst_cluster_id])
            return

        self.cluster_recy_tasks[dst_cluster_id] -= 1
        print('remove count', self.cluster_recy_tasks[dst_cluster_id])

    def add_running_task(self, task):
        if not self.is_recovery_task(task):
            return

        print('remove_running_task task:%s ', task.get_cfg()['name'])
        dst_cluster_id = self.get_task_dst_cluster_id(task)
        print('task: %s add to cluster: %s', task.id, dst_cluster_id)

        self.cluster_recy_tasks[dst_cluster_id] += 1
#         print('add count', self.cluster_recy_tasks[dst_cluster_id])
