# -*- coding: utf-8 -*-

# import hcommon
from hcommon import show_list
from pack import math
from pack.math import sub


class Tmp(object):
    import uuid     # import to class membor
    def get_uuid(self):
        return str(self.uuid.uuid4())


def import_tt():
    print("import_tt start")
#     hcommon.show_list([1, 2])
    show_list([1, 2])
    print(math.add(1, 2))
    print(sub(3, 2))


def import_func():
#     import hcommon.show_list2 as show_list2
#     show_list2([1, 2])
    
    hcommon = __import__('hcommon', fromlist=True)
    hcommon.show_list2([1, 2])


def import_position_tt():
    tmp = Tmp()
    print(tmp.get_uuid())
    

if __name__ == "__main__":
#     import_tt()
#     import_func()
    import_position_tt()
