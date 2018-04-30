# -*- coding: utf-8 -*-

clsMgr = {}

def wrapper_mgr(key):
    def register(cls):
        print("register", key, cls.__name__)
        clsMgr[key] = cls
        return cls

    return register(cls)


@wrapper_mgr("HongKey")
class ManHong:
    def __init__(self):
        print(type(self))



def run():
    pass


if __name__ == "__main__":
    run()
    

