# -*- coding: utf-8 -*-

import sys


def run():
    reload(sys)
    print("before default encoding: %s" % sys.getdefaultencoding())
    sys.setdefaultencoding("utf-8")
    print("after change default encoding: %s" % sys.getdefaultencoding())
    print("===============")

    name = "洪"
    print(type(name), name)
    print(name)
    print(len(name))

    dname = name.decode()
    print(type(dname), dname)
    print(dname)
    print(len(dname))

    ename = dname.encode()
    print(type(ename), ename)
    print(ename)
    print(len(ename))

    print("===============")


if __name__ == "__main__":
    run()
