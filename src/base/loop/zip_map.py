# -*- coding: utf-8 -*-

def zip_tt():
    L1 = [1, 2, 3, 4]
    L2 = [11, 22, 33]

    z = zip(L1, L2)
    print(type(z), type(z[0]), z)
    print(zip(z))


# python3 map is generator
def map_tt():
    L1 = [1, 2, 3, 4]
    L2 = [11, 22, 33]
    print(map(None, L1, L2))


def run():
    zip_tt()
    map_tt()


if __name__ == "__main__":
    run()
