# -*- coding: utf-8 -*-

import contextlib


@contextlib.contextmanager
def make_list():
    print("make list start")
    l = []
    l.append(0)
    try:
        yield l
    finally:
        print("make list end")
        l.append(len(l))


def with_tt():
    with make_list() as li:
        li.append(2)
    print(li)


def run():
    with_tt()


if __name__ == "__main__":
    run()
