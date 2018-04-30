# -*- coding: utf-8 -*-
'''
Created on 2018年4月14日

@author: jason
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column, 
    Integer, String, TIMESTAMP,
    ForeignKey, UniqueConstraint, Index,
)
from sqlalchemy.orm import (
    sessionmaker,
    relationship,
)

db_url = 'mysql+mysqldb://root:hong@127.0.0.1:3306/user_permission'
engine = create_engine(db_url, max_overflow=5, echo=False)
Base = declarative_base()


class DBUser(Base):
    __tablename__ = 't_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(16), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(40), nullable=False)
    created = Column(TIMESTAMP)


class DBGroup(Base):
    __tablename__ = 't_group'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(16), unique=True, nullable=False)


class DBPermission(Base):
    __tablename__ = 't_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    permission_name = Column(String(16), unique=True, nullable=False)


class DBUserGroup(Base):
        __tablename__ = 't_user'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    permission_name = Column(String(16), unique=True, nullable=False)
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
        
if __name__ == '__main__':
    pass