# -*- coding: utf-8 -*-


def lambda_tt():
    func = lambda x, y: x + y
    print(func(1, 2))

    func = lambda s1="abc", s2="ABC": s1 + s2
    print(func("111"))
    print("=========")

    l = [lambda x: x * 2,
         lambda x: x * 3,
         lambda x: x * 4]
    for func in l:
        print(func(2))

    print("=========")

    d = {"one" : lambda: 1,
         "two" : lambda: 2}
    print(d["one"]())


def lambda_tt2():
    def add(x):
        return (lambda y: x + y)

    func = add(1)
    print(type(func), func, func(2))


def run():
    lambda_tt()
    lambda_tt2()


if __name__ == "__main__":
    run()
    

