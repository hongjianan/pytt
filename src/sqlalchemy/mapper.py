# encoding: utf-8
'''
Created on 2018年4月13日

@author: Hong
'''

from sqlalchemy.orm import (
	mapper,
)

from db_mgr import DBMgr
from orm_object import DBUser

def mapper_tt():
	mgr = DBMgr()
	mgr.define_tables_user()
	mgr.create_table()
	
	mapper(DBUser, mgr.user_table)

def create():
	user = DBUser()
	user.user_name = 'jason'
	user.password = 'password'
	user.email = 'hjnhong@163.com'
	
	mgr.session.add(user)
	mgr.session.flush()
	mgr.session.commit()
	

def query():
	
	
if __name__ == '__main__':
	mapper_tt()
	