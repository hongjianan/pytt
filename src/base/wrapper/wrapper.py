# coding: UTF-8

import time


def WrapperTimer(func):
    def timer():
        start = time.time()
        func()
        end = time.time()
        print("func=%s time=%fms" % (func.__name__, (end - start) * 1000))
    return timer

def sleepy():
    print("sleeping ...")
    time.sleep(1)
    print("exit")

print("before func name=%s" % sleepy.__name__)
sleepy = WrapperTimer(sleepy)
print("after func name=%s" % sleepy.__name__)


# 使用@语法糖
@WrapperTimer
# xxx
def sleeps():
    print("sleep time=0.5")
    time.sleep(0.5)
    print("exit")


def WrapperTimers(func):
    def timer(time_s):
        start = time.time()
        func(time_s)
        end = time.time()
        print("func=%s time=%fms" % (func.__name__, (end - start) * 1000))
    return timer


@WrapperTimers
def sleep_time(time_s):
    print("sleep_time time=%d" % time_s)
    time.sleep(time_s)
    print("exit")


# 装饰器带参数
def WrapperArgs(arg = True):
    if arg:
        def wrapper(func):
            def timer(time_s):
                start = time.time()
                func(time_s)
                end = time.time()
                print("func=%s time=%fms" % (func.__name__, (end - start) * 1000))
            return timer
    else:
        def wrapper(func):
            def timer(time_s):
                print("func=%s no time" % func.__name__)
                func(time_s)
            return timer
    return wrapper


@WrapperArgs(True)
def sleep_time_open(time_s):
    print("sleep_time time=%d" % time_s)
    time.sleep(time_s)
    print("exit")


@WrapperArgs(False)
def sleep_time_close(time_s):
    print("sleep_time time=%d" % time_s)
    time.sleep(time_s)
    print("exit")


# def WrapperPrintBool(bool):
#     def wrapper():



def run():
    # sleepy()
    sleeps()
    # sleep_time(1)
    # sleep_time_open(1)
    # sleep_time_close(1)


if __name__ == "__main__":
    run()
