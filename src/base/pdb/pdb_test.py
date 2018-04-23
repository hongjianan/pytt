# coding: UTF-8

import pdb

def trace_tt():
    a = 1
    pdb.set_trace()
    a = 2


def run():
    trace_tt()
    # reflect_tt()


if __name__ == "__main__":
    run()
