# coding: UTF-8


def fib(times):
    now = 1
    next = 1
    while times > 0:
        times -= 1
        yield now
        tmp = next
        next += now
        now = tmp


def xrange(start, end, distance = 1)

def filb_tt():
    for i in fib(10):
        print(i)
    range(10)

def run():
    filb_tt()


if __name__ == "__main__":
    run()
    

