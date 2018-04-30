# -*- coding: utf-8 -*-
'''
Created on 2018年4月14日

@author: jason
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
    TIMESTAMP,
    create_engine,
    ForeignKey,
)
from sqlalchemy.orm import (
    sessionmaker,
)


class DBUPMgr():
    def __init__(self, echo=False):
        self.db_url = 'mysql+mysqldb://root:hong@127.0.0.1:3306/user_permission'
        # create engine
        print('create engine=%s' % self.db_url)
        self.engine = create_engine(self.db_url, max_overflow=5, echo=echo)
        self.metadata = MetaData()
        
        # create session
        print('create database session.')
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        
        # define tables
        self.__define_tables()
        
    def __define_tables(self):
        self.t_user = Table(
            't_user', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('user_name', String(16), unique=True, nullable=False),
            Column('email', String(255), unique=True, nullable=False),
            Column('password', String(40), nullable=False),
            Column('created', TIMESTAMP),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        self.t_group = Table(
            't_group', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('group_name', String(16), unique=True, nullable=False),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        self.t_permission = Table(
            't_permission', self.metadata,
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('permission_name', String(16), unique=True, nullable=False),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        self.t_user_group = Table(
            't_user_group', self.metadata,
            Column('user_id', Integer, ForeignKey('t_user.id'), primary_key=True),
            Column('group_id', Integer, ForeignKey('t_group.id'), primary_key=True),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        self.t_group_permission = Table(
            't_group_permission', self.metadata,
            Column('group_id', Integer, ForeignKey('t_group.id'), primary_key=True),
            Column('permission_id', Integer, ForeignKey('t_permission.id'), primary_key=True),
            mysql_engine='InnoDB',
            mysql_charset='utf8',
        )
        
        
    def create_table(self):
        ''' 当数据库已经存在这张表时，将不会创建、修改这张表的数据
        '''
        self.metadata.create_all(self.engine)


def create_table():
    mgr = DBUPMgr(echo=True)
    mgr.create_table()
    
          
if __name__ == '__main__':
    create_table()
    
    