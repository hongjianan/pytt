# -*- coding: utf-8 -*-
'''
Created on 2018年10月16日

@author: Jason
'''
import struct


class Struct(object):
    def __init__(self, *args, **kwargs):
        self.buf = None
        self.items = list()
    
    def set_items(self):
        pass

    def pack(self):
        # get fmts
        fmts = ''
        for fmt in self.items:
            fmts += fmt[0]
        # get values
        values = [val[1] for val in self.items]
        
        self.buf = struct.pack(fmts, *values)
        return self.buf
    
    def unpack(self):
        pass
    
    def size(self):
        pass


class Person(Struct):
    
    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.name = ('3s', 'hjn')
        self.age = ('i', kwargs.get('age', None))
        self.set_items()
        
    def set_items(self):
        self.items = (self.name, self.age)
    

def struct_tt():
    bin_buf = struct.pack('i', 0x1111ffff)
    with open('data', 'wb') as f:
        p = Person(age=0x111122ff)
        p.pack()
        f.write(p.buf)
        print(p.buf)


if __name__ == '__main__':
    struct_tt()
