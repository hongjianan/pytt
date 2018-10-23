# -*- coding: utf-8 -*-
'''
Created on 2018年9月16日

@author: Jason
'''
import time
from pymongo import Connection

db = Connection().jason
stu = db.stu

datas = stu.find()
print(datas)



if __name__ == '__main__':
    pass