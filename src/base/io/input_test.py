# -*- coding: utf-8 -*-

import getpass


def raw_input_tt1():
    username = raw_input("username:").strip()
    password = getpass.getpass("password:")
    print(username, password)


def raw_input_tt2():
    name = raw_input('name:')
    print(name)
    

def input_tt2():
    name = raw_input()
    print(name)
    

if __name__ == "__main__":
#     raw_input_tt1()
    raw_input_tt2()
