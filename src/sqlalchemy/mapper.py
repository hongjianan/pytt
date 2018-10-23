# -*- coding: utf-8 -*-
'''
Created on 2018年4月13日

@author: Hong
'''

from sqlalchemy.orm import (
    mapper,
)

from db_mgr import DBMgr
from orm_object import DBUser


def create_table():
    mgr = DBMgr()
    mgr.define_table_user()
    mgr.create_table()

def create_record():
    mgr = DBMgr()
    mgr.define_table_user()
    mapper(DBUser, mgr.user_table)
    
    user = DBUser()
    user.user_name = 'jason'
    user.password = 'password'
    user.email = 'hjnhong@163.com'
    
#     mgr.session.add(user)
#     mgr.session.flush()
#     mgr.session.commit()
    

def query():
    pass
    
if __name__ == '__main__':
    create_table()
    