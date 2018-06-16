# -*- coding: utf-8 -*-
'''
Created on 2018年5月7日

@author: Administrator
'''

from collections import namedtuple

def tuple_tt():
    user = ('jason', 27, True)
    # name, *other = user    # python3
    name, age, gender = user
    print(name, age, gender)
    
    # 如果tuple中保存的是list等对象，只要不修改list的索引，就能修改其中list的数据
    nums = ([1, 3, 5],
            [2, 4, 6])
    print(nums)
    nums[0].append(7)
    print('tuple after change', nums)
    
    print('=========')
    
    xy = ((0, 1),
          (2, 3))
    print(xy[0][0])
    print(xy[0][1])

    if False:
        xyz = [[[],],]
        xyz[True][False][True] = (1, 0, 1)
        xyz[False][False][True] = (0, 0, 1)
        
        print(xyz[True][False][True])
    


def namedtuple_tt():
    Point = namedtuple('point3', ['x', 'y', 'z'])
    a = Point(1, 2, 3)
    b = Point(x=4, y=5, z=6)
    d = Point._make((10, 20, 30))
    print(a)
    print(b)
    print(d)
    print(a.x, a.y, a.z)
    print("getattr(a, 'x')", getattr(a, 'x'))
    print("hasattr(a, 'x')", hasattr(a, 'x'))
    print("hasattr(a, 'xy')", hasattr(a, 'xy'))
    print("hasattr(Point, 'x)", hasattr(Point, 'x'))
    # asdict
    dd = d._asdict()
    print(type(dd), dd)
    
    # tuple hashable
    d = {}
    d[a] = 1
    print(d[a])

if __name__ == '__main__':
#     tuple_tt()
    namedtuple_tt()
    