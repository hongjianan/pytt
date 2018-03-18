# coding: UTF-8

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


if __name__ == "__main__":
    run()

