# -*- coding: utf-8 -*-

NAME = "hong"


def func1():
    global NAME
    print(NAME)

    name = "hjn"
    NAME = "nan"
    print(name, NAME)


def func2():
    print(NAME)


def run():
    func1()
    func2()


if __name__ == "__main__":
    run()
    

