# coding: UTF-8


class WhatFor(object):
    def it(cls):
        print('work with %s' % cls)

    it = classmethod(it)

    def uncommon():
        print('I could be a global function')

    uncommon = staticmethod(uncommon)


def internal_tt():
    obj = WhatFor()
    obj.it()
    obj.uncommon()


if  __name__ == '__main__':
    internal_tt()
