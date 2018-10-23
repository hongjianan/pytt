# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: Administrator
'''

import tensorflow as tf

def test():
    import pdb; pdb.set_trace()
    a = tf.constant([1, 2], name="a", dtype=tf.float32)
    b = tf.constant([2.0, 3.0], name="b")
    c = a + b
    print(c)


if __name__ == '__main__':
    test()
