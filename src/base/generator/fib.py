# coding: UTF-8


def fib():
    now, after = 0, 1
    while True:
        yield now
        now, after = after, now + after


def filb_tt():
    f = fib()
    li = [f.next() for i in range(10)]
    print(li)


def run():
    filb_tt()


if __name__ == "__main__":
    run()
    

