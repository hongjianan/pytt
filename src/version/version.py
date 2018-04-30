# -*- coding: utf-8 -*-

import sys


verno = int(sys.version[0])


def run():
    if 2 == verno:
        print("this is version 2")
    else:
        print("this is version 3")


if __name__ == "__main__":
    run()
