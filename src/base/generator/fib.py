# coding: UTF-8


def fib(times):
    now = 1
    next = 1
    while times > 0:
        times -= 1
        yield now
        now, next = next, now + next


def filb_tt():
    for i in fib(10):
        print(i)
    range(10)


def run():
    filb_tt()


if __name__ == "__main__":
    run()
    

