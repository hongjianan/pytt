# -*- coding: utf-8 -*-

import pymongo


def mongo_tt():
    mc = pymongo.MongoClient("mongodb://192.168.1.131:27017")
    # mc = pymongo.MongoClient("mongodb://user:pwd@192.168.1.131:27017/db_name")

    # 指定数据库
    db = mc.jason
    # print("========== db doc =========")
    # print(dir(db))
    # print("========== db doc =========")

    # 指定集合
    stu = db.stu
    # print("========== collection doc =========")
    # print(dir(stu))
    # print("========== collection doc =========")

    # 增 insert_one  insert_many
    # stu.insert_one({"name":"jason", "age": 30, "gender" : 2})

    # 改
    # stu.update_one({"name": "jason"}, {"$set": {"age": 28}})

    # 删
    stu.delete_one({"name": "jason"})

    # 查 find_one()   find()
    # cursor = stu.find()
    # for line in cursor:
    #     print(line)

    # 排序
    cursor = stu.find({"age" : {"$gt": 10}}).sort("name", pymongo.ASCENDING).skip(0).limit(2)
    for line in cursor:
        print(line)

def run():
    mongo_tt()


if __name__ == "__main__":
    run()
