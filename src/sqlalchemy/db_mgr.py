# encoding: utf-8
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
	def __init__(self):
		self.db_url = 'mysql://192.168.1.131:3306/'
		# create engine
		self.engine = create_engine(self.db_url, echo=True)
		self.metadata = MetaData()
		
		# create session
		Session = sessionmaker()
		Session.configure(bind=self.engine)
		self.session = Session()
		
		# define tables
		self.user_table = None
		
	def define_tables_user(self):
		self.user_table = Table(
			't_user', self.metadata,
			Column('uid', Integer, primary_key=True, autoincrement=True),
			Column('user_name', Unicode(64), nullable=False),
			Column('password', String(64), nullable=False),
			Column('email', String(64), unique=True, nullable=False),
			Column('create_time', DateTime, default=datetime.datetime.utcnow, nullable=False),
			Column('update_time', DateTime),
		)
		
	def create_table(self):
		self.metadata.create_all(self.engine)
		
		
if __name__ == '__main__':
	pass