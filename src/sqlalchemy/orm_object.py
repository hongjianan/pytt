# -*- coding: utf-8 -*-
'''
Created on 2018年4月13日

@author: Hong
'''
import time

from sqlalchemy.orm import (
    mapper,
)

import db_mgr

class DBUser(object):
    pass
    

class ORMCtrl():
    def __init__(self, dbmgr):
        self.dbmgr = dbmgr
        self.dbmgr.define_table_user()
        
    def mapper_user(self):
        mapper(DBUser, self.dbmgr.t_user)
        
        
def create_tt():
    mgr = db_mgr.DBMgr()
    ctrl = ORMCtrl(mgr)
    ctrl.mapper_user()
    
    user = DBUser()
    user.user_name = 'jason'
    user.password = 'test'
    user.email = 'hjnhong@163.com'
    
    mgr.session.add(user)
#     mgr.session.flush()
#     mgr.session.commit()

def query_tt():
    mgr = db_mgr.DBMgr()
    ctrl = ORMCtrl(mgr)
    ctrl.mapper_user()
    
    query = mgr.session.query(DBUser)    # query 就是 select
    print(query)
    user_first = query.first()
    print('=== user_first ===', user_first.__dict__)
    
    user_pk_2 = query.get(2)
    print('=== user_pk_2 ===', user_pk_2.__dict__)
    
    user_jason = query.filter_by(user_name='jason').one()
    print('=== user_jason ===', user_jason.__dict__)
    

def order_tt():
    mgr = db_mgr.DBMgr()
    ctrl = ORMCtrl(mgr)
    ctrl.mapper_user()

    query = mgr.session.query(DBUser)    # query 就是 select
    
    for user in query.order_by(DBUser.uid):
        print(user.uid, user.user_name)
        
        
def update_tt():
    mgr = db_mgr.DBMgr()
    ctrl = ORMCtrl(mgr)
    ctrl.mapper_user()
    
    query_user = mgr.session.query(DBUser)    # query 就是 select
    user = query_user.get(2)
    user.password = 'pwtest'
    mgr.session.commit() 


if __name__ == '__main__':
#     create_tt()
#     query_tt()
    order_tt()
#     update_tt()
    