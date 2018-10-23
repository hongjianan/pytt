# -*- coding: utf-8 -*-
'''
Created on 2018年4月28日

@author: Hong
'''

from enum import (
    Enum,
    unique
)


class SwitchState(Enum):
    OPEN = 'open'
    CLOSE = 'close'
    
    @property
    def OPEN(self):
        return SwitchState.__OPEN
    
    @property
    def CLOSE(self):
        return SwitchState.__CLOSE.value


class TaskState(Enum):
    WAITING = 0
    DOING = 1
    CANCELING = 2
    CANCELED = 3
    FAIL = 4
    FINISH = 5

    @classmethod
    def values(cls):
        return (cls.WAITING, cls.DOING, cls.CANCELING,
                cls.CANCELED, cls.FAIL, cls.FINISH)

ULOG_STATE = {
    'DOING': TaskState.DOING,
    'WAITING': TaskState.WAITING,
    'CANCELING': TaskState.CANCELING,
    'CANCELED': TaskState.CANCELED,
    'FINISH': TaskState.FINISH,
}


# @unique # if wrapper unique, red_alis != 1
class Color(Enum):
    red = 1
    yellow = 2
    blue = 3
    red_alis = 1
    
    
def enum_tt():
    print(type(Color.red))
    
    print('Color.red', Color.red)
    print(Color(1))
    print(Color['red'])
    print(Color.red.name)
    print(Color.red.value)
    
    if Color.red == Color.red_alis:
        print('Color.red == Color.red_alis')
    else:
        print('Color.red != Color.red_alis')
        
    for i in Color:
        print(i, i.value)
        
    print(type(Color.__members__))
    for k, v in Color.__members__.items():
        print(k)
        print(v)
        
    for k, v in ULOG_STATE.items():
        print(k, v.value)
    

def enum_class_tt():
    print(type(TaskState.WAITING), TaskState.WAITING.value)
    print(type(SwitchState().OPEN), SwitchState().OPEN)

    
def use_tt():
    light = Color.red
    print(light, light.name, light.value)
    print('light is red', light == Color.red)
    
if __name__ == '__main__':
#     enum_tt()
#     use_tt()
    enum_class_tt()
    