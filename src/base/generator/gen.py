# coding: UTF-8


def gen_num(start, end, distance):
    print("start gen_num")
    while start < end:
        value = yield start
        value += distance
        start = value


def run():
    num = (x * x for x in range(0, 10, 2))
    while True:
        try:
            print(num.next())
            print(next(num))
        except Exception as e:
            print("generator end", e.message)
            break

    print("===================")

    num = (x * x for x in range(0, 10, 2))
    for i in num:
        print(i)

    print("===================")

    num = gen_num(0, 10, 2)
    while True:
        try:
            print(num.next())
            # print(next(num))
            print(num.send(3))
        except Exception as e:
            print("generator end", e.message)
            break


if __name__ == "__main__":
    run()

