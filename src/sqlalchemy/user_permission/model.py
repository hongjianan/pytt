# -*- coding: utf-8 -*-
'''
Created on 2018年4月14日

@author: jason
'''

from sqlalchemy.orm import (
    mapper,
    relation,
)


class DBUser(object):
    groups = []


class DBGroup(object):
    permissions = []


class DBPermission(object):
    pass


class DBUserGroup(object):
    pass


class DBGroupPermission(object):
    pass


mgr = sql.DBUPMgr()

mapper(DBUser, mgr.t_user, 
       properties=dict(groups=relation(DBGroup, secondary=user_group, backref=’users’)))

mapper(DBGroup, mgr.t_group, 
       properties=dict(permissions=relation(DBPermission, secondary=group_permission, backref=’groups’)))

mapper(DBPermission, mgr.t_permission)


if __name__ == '__main__':
    pass