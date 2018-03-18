# coding: UTF-8

import getpass


def input_tt():
    username = raw_input("username:").strip()
    password = getpass.getpass("password:")
    print(username, password)


def run():
    input_tt()


if __name__ == "__main__":
    run()
    

