# coding: UTF-8

import sys
import re


def re_tt():
    '''
    compile, match, search, findall, finditer, split
    :return:
    '''
    pattern = re.compile(r"\d")
    ma = pattern.match("123")
    print(ma.group())

    pattern = re.compile(r"\d+")
    ma = pattern.match("123")
    print(ma.group())

    # 分组 group
    pattern = re.compile(r"([a-z]+) ([a-z]+)", re.I)
    ma = pattern.match("hello world nihao python")
    print(0, ma.group(0), ma.span(0))
    print(1, ma.group(1), ma.span(1))
    print(2, ma.group(2), ma.span(2))

    pattern = re.compile(r"\d+")
    ma = pattern.search("aaa123bb456")
    print(0, ma.group(0), ma.span(0))

    pattern = re.compile(r"\d?")
    print(0, pattern.findall("aaa 123 456"))

    pattern = re.compile(r"\d+")
    print(0, pattern.findall("aaa 123 456"))
    ma = pattern.finditer("aaa 123 456")

    mb = ma
    for i in ma:
        print(i.group())

    for i in mb:
        print(i.group())




def run():
    re_tt()

if __name__ == "__main__":
    run()
