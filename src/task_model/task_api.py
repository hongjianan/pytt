# coding=utf-8
# !/usr/bin/env python2
import uuid

COMPLETE = 3  # 任务状态为完成中
WAITING = 2  # 任务状态为等待中
RUNNING = 1  # 任务状态为运行中
CANCELLED = 0  # 任务状态为取消


class ITask(object):
    __task_type__ = ""

    def __init__(self):
        self.cfg = dict()   # 配置的信息，调度的时候可以根据task的额外信息进行判断
        self.task_id = str(uuid.uuid1())
        self.task_status = WAITING
        self.deadline = None
        self.timeout_cancel = False
        self.priority_level = 0

    @property
    def id(self):
        return self.task_id

    @id.setter
    def id(self, value):
        self.task_id = value

    def set_cfg(self, cfg):
        self.cfg = cfg

    def get_cfg(self):
        return self.cfg

    def get_type(self):
        return self.__task_type__
    
    def catch_run(self, **kwargs):
        try:
            self.run(**kwargs)
        except Exception:
#             print('task: %s exit', self)
            self.exit()
            raise

#         print('task: %s exit', self)
        self.exit()

    def run(self, **kwargs):
        raise NotImplementedError
    
    def exit(self):
        self.task_status = COMPLETE
        
    def is_exit(self):
        return self.task_status == COMPLETE
    
    def _get_ulog_state(self, request_context):
        if request_context is None:
            request_context = get_admin_context()
        ulog = get_ulog(request_context, self.id)
        ulog = ulog['ulog']
        return ulog['state']

    def is_task_cancelled(self, request_context=None):
        if self.task_status == CANCELLED:
            return True
        elif self.task_status == RUNNING:
            try:
                ulog_state = self._get_ulog_state(request_context)
                if ulog_state == "canceling":
                    self.task_status = CANCELLED
                    return True
            except Exception as ex:
                LOG.exception(ex)
            return False
        else:
            return False
