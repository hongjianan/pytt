# -*- coding: utf-8 -*-


def enumerate_tt():
    name = "abcdef"

    for (i, v) in enumerate(name):
        print(i, v)


def enumerate_gen():
    gen = enumerate("abcdef")
    print(type(gen))
    while True:
        try:
            print(gen.next())
        except Exception as e:
            print("gen end", e)
            break


def run():
    enumerate_tt()
    enumerate_gen()


if __name__ == "__main__":
    run()
    

