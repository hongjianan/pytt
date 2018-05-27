# -*- coding: utf-8 -*-

import contextlib
import uuid


class Log(object):
    def __init__(self, lid=None):
        self.lid = lid
    
    def __enter__(self):
        print('__enter__')
        if not self.lid:
            self.lid = str(uuid.uuid4())
        return []
        
    def __exit__(self, type, value, trace):
        print(type, value, trace)
        print('__exit__')
        self.lid = None
        
    def get_id(self):
        return self.lid


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

def enter_tt():
#     with Log() as l:
#         print(type(l))
#         print(l.get_id())
    
    print('======')
    l = Log()
    l.__enter__()
    print(l.get_id())
    l.__exit__(None, None, None)
    
    print('======')
    l = Log()
    
    with l:
        print(l.get_id())


if __name__ == "__main__":
#     with_tt()
    enter_tt()
