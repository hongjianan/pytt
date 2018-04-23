# encoding: UTF-8
'''
Created on 2018年4月14日

@author: jason
'''

from sqlalchemy import (
    create_engine,
)

def engine_insert_tt():
    db_url = 'mysql+mysqldb://root:hong@127.0.0.1:3306/user_permission'
    engine = create_engine(db_url, max_overflow=5, echo=False)
    
    cursor = engine.execute('insert into t_user(user_name, password, email) value(%(name)s, %(pwd)s, %(email)s)', 
        name='jason', pwd='123', email='jason@qq.com')
    print(cursor.__dict__)
    
    cursor = engine.execute('insert into t_user(user_name, password, email) value(%s, %s, %s)', 
        ['lixiang', '123', 'lixiang@qq.com'])
    print(cursor.__dict__)
    
    cursor = engine.execute('insert into t_user(user_name, password, email) value(%s, %s, %s)', 
        (['hongjianan', '123', 'hongjianan@qq.com'], ['xiaohong', '123', 'xiaohong@qq.com'], ))
    print(cursor.__dict__)

def engine_select_tt():
    db_url = 'mysql+mysqldb://root:hong@127.0.0.1:3306/user_permission'
    engine = create_engine(db_url, max_overflow=5, echo=False)
    
    cursor = engine.execute('select * from t_user')
    print(cursor.__dict__)
    print(cursor.cursor.__dict__)
    print('====================')
    
    users = cursor.fetchone()
    print(users)
    users = cursor.fetchmany(2)
    print(users)
    users = cursor.fetchall()
    print(users)
        

if __name__ == '__main__':
#     engine_insert_tt()
    engine_select_tt()
    