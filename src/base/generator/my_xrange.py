# coding: UTF-8
import time

def my_xrange(*args):
    start = 0
    step = 1
    if 1 == len(args):
        end = args[0]
    elif 2 == len(args):
        start = args[0]
        end = args[1]
    elif 3 == len(args):
        start = args[0]
        end = args[1]
        step = args[2]

    while start < end:
        restart = yield start
        if None == restart:
            start += step
        else:
            start = restart


def run():
    gen = my_xrange(0, 10)

    print(gen.next())
    print(gen.send(3))
    print(gen.send(None))


def range_time():
    # time.sleep(3)
    begin = time.time()
    a = 0
    for i in range(1000 * 1000):
        a += i
    delta = time.time() - begin
    print('range using time:', delta)
    # time.sleep(3)
    #==================================
    begin = time.time()
    a = 0
    for i in xrange(1000 * 1000):
        a += i
    delta = time.time() - begin
    print('xrange using time:', delta)
    # time.sleep(3)


if __name__ == "__main__":
    # run()
    range_time()
