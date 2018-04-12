# coding: UTF-8

USER_NAME = "jason"
USER_AGE = 27


def WrapperPrinter1(func):
    def wrapper1(*args, **kwargs):
        print("===== 1 =====running %s ..." % func.__name__)
        ret = func(*args, **kwargs)
        return ret
    # wrapper.__name__ = func.__name__
    return wrapper1


def WrapperPrinter2(func):
    def wrapper2(*args, **kwargs):
        print("===== 2 =====running %s ..." % func.__name__)
        ret = func(*args, **kwargs)
        return ret
    # wrapper.__name__ = func.__name__
    return wrapper2


# 装饰器越上层越底层
@WrapperPrinter2
@WrapperPrinter1
def get_user():
    print("user name=%s age=%d" % (USER_NAME, USER_AGE))


# @WrapperPrinter1
def set_user(name, age = 27):
    global USER_NAME, USER_AGE
    USER_NAME = name
    USER_AGE = age
    print("set user, name=%s age=%d" % (name, age))

set_user = WrapperPrinter2(set_user)
set_user = WrapperPrinter1(set_user)


def run():
    get_user()
    print(get_user.__name__)

    set_user("hongjianan")
    get_user()

    set_user("lixiang", 20)
    get_user()


if __name__ == "__main__":
    run()
