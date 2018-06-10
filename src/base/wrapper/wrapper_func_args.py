# -*- coding: utf-8 -*-

USER_NAME = "jason"
USER_AGE = 27


def WrapperPrinter1(func):
    print('==init WrapperPrinter1==')
    def wrapper1(*args, **kwargs):
        print("===== 1 =====running %s ..." % func.__name__)
        ret = func(*args, **kwargs)
        return ret
#     wrapper1.__name__ = func.__name__
    return wrapper1


def WrapperPrinter2(func):
    print('==init WrapperPrinter2==')
    def wrapper2(*args, **kwargs):
        print("===== 2 =====running %s ..." % func.__name__)
        ret = func(*args, **kwargs)
        return ret
    wrapper2.__name__ = func.__name__
    return wrapper2


print('======order1=========')
'''
装饰器越上层越底层
equal to:
    get_user = WrapperPrinter1(get_user)
    get_user = WrapperPrinter2(get_user)
'''
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

print('======order2=========')
set_user = WrapperPrinter2(set_user)
set_user = WrapperPrinter1(set_user)


def call_order_tt():
    get_user()
    print(get_user.__name__)


def call2_order_tt():
    set_user("hongjianan")
    get_user()

#     set_user("lixiang", 20)
#     get_user()


if __name__ == "__main__":
#     call_order_tt()
    call2_order_tt()
