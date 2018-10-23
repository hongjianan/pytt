# coding=utf-8
# !/usr/bin/env python2
from cloudmanagerclient.client import Client
from phoenix.common.context import RequestContext


def get_ulog(request_context, task_id):
    client = Client.get_sf_noauth_client(
        user_id=request_context.user_id,
        project_id=request_context.project_id,
        # 内部接口，无法精确取到用户角色，直接置admin
        roles='admin'
    )
    ulog = client.ulog.show_ulog(task_id)
    return ulog


def get_admin_context():
    params = {
        'roles': ['admin'],
        'user_id': '227934a42e3442b49f759c10a2d59b26',  # 对应的用户不存在
        'project_id': '227934a42e3442b49f759c10a2d59b26',  # 对应组织不存在
        'sf_ulog': ''
    }
    return RequestContext.from_dict(params)
