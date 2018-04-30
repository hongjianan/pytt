# -*- coding: utf-8 -*-
'''
Created on 2018年4月15日

@author: Hong
'''

from sql import (
	session,
	Users,
	Favor,
	Person,
	ServerToGroup,
	Group,
	Server,
)

def op_create():
	session.add(Users(name="alex0", extra='sb'))
	
	session.add_all([
		Users(name="alex1", extra='sb'),
    	Users(name="alex2", extra='sb'),
	])
	session.commit()	# 这里需要commit，不然不提交数据


def op_delete():
	result = session.query(Users).filter(Users.id > 2).delete()
	print(type(result))	# <type 'long'>
	session.commit()


def op_update():
	session.query(Users).filter(Users.id == 2).update({"name" : "099"})
	
	'''
2018-04-15 21:49:57,554 INFO sqlalchemy.engine.base.Engine UPDATE users SET name=(concat(users.name, %s)) WHERE users.id = %s
2018-04-15 21:49:57,554 INFO sqlalchemy.engine.base.Engine ('099', 2)
	'''
	session.query(Users).filter(Users.id == 2).update({Users.name: Users.name + "099"}, synchronize_session=False)

# 	session.query(Users).filter(Users.id == 2).update({"num": Users.num + 1}, synchronize_session="evaluate")
	session.commit()


def op_query():
	'''
	SELECT users.name AS users_name, users.extra AS users_extra 
	FROM users
	'''
	ret = session.query(Users).all()
	print('1=====', ret)
	
	'''
	SELECT users.name AS users_name, users.extra AS users_extra 
	FROM users
	'''
	ret = session.query(Users.name, Users.extra).all()
	print('2=====', ret)
	
	'''
	SELECT users.id AS users_id, users.name AS users_name, users.extra AS users_extra 
	FROM users 
	WHERE users.name = %s
	'''
	ret = session.query(Users).filter_by(name='alex0').all()
	print('3=====', ret)
	
	'''
	SELECT users.id AS users_id, users.name AS users_name, users.extra AS users_extra 
	FROM users 
	WHERE users.name = %s 
 	LIMIT %s
	'''
	ret = session.query(Users).filter_by(name='alex0').first()
	print('4=====', ret)
	

def op_condition():
	
# 	ret = session.query(Users).filter_by(name='alex0').all()
# 	for user in ret:
# 		print('1=====', user.__dict__)

	''' AND
	WHERE users.id > %s AND users.name = %s
	'''
# 	ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
#  	for user in ret:
#  		print('2=====', user.__dict__)
 	
 	''' AND, BETWEEN
 	WHERE users.id BETWEEN %s AND %s AND users.name = %s
 	'''
 	ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'alex0')  # 这里的加不加 all()都一样
 	for user in ret:
  		print('3=====', user.__dict__)
  		
#   	ret = session.query(Users).filter(Users.id.in_([1,3,4])).all()

if __name__ == '__main__':
# 	op_create()
# 	op_delete()
# 	op_update()
# 	op_query()
	op_condition()
	
	
	