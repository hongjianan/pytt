# coding: UTF-8

import sys


def sys_tt():
    print(dir(sys))

    print("sys.argv", sys.argv)

    # 模块搜索路径
    print("sys.path", sys.path)

    print("sys.version", sys.version)

    print("sys.platform", sys.platform)

    sys.stdout.write("sys.stdout.write\n")

    sys.stdout.write("please input line:")
    input = sys.stdin.readline()
    print("input", input)


    exit("byebye")
    # sys.exit(0)


def run():
    sys_tt()


if __name__ == "__main__":
    run()
