# coding: UTF-8

# import hcommon
from hcommon import show_list
from pack import math
from pack.math import sub

def import_tt():
    print("import_tt start")
#     hcommon.show_list([1, 2])
    show_list([1, 2])
    print(math.add(1, 2))
    print(sub(3, 2))

def run():
    import_tt()


if __name__ == "__main__":
    run()
    

