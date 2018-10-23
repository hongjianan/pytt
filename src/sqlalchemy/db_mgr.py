# -*- coding: utf-8 -*-
'''
Created on 2018年4月12日

@author: Hong
'''
import datetime

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Unicode,
    DateTime,
    create_engine,
)
from sqlalchemy.orm import (
    sessionmaker,
)


class DBMgr():
    def __init__(self, echo=False):
        self.db_url = 'mysql+mysqldb://root:hong@127.0.0.1:3306/test'
        # create engine
        print('create engine=%s' % self.db_url)
        self.engine = create_engine(self.db_url, echo=echo)
        self.metadata = MetaData()
        
        # create session
        print('create database session.')
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        
        # define tables
        self.t_user = None
        
    def define_table_user(self):
        self.t_user = Table(
            't_user', self.metadata,
            Column('uid', Integer, primary_key=True, autoincrement=True),
            Column('user_name', Unicode(64), nullable=False),
            Column('password', String(64), nullable=False),
            Column('email', String(64), unique=True, nullable=False),
            Column('create_time', DateTime, default=datetime.datetime.utcnow, nullable=False),
            Column('update_time', DateTime),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        
    def create_table(self):
        self.metadata.create_all(self.engine)
        

def table_tt():
    mgr = DBMgr()
    mgr.define_table_user()
    mgr.create_table()
    
        
if __name__ == '__main__':
    table_tt()

