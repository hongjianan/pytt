# coding: UTF-8


def open_tt():
    # r: 只读，默认
    # w: 只写，不存在创建，存在清空
    # x: 只写，不存在创建，存在报错
    # a: 追加
    f = open("test.file", "w+")
    f.write("nihao")


def run():
    open_tt()


if __name__ == "__main__":
    run()
    

