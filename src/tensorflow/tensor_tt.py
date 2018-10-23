# -*- coding: utf-8 -*-
'''
Created on 2018年10月22日

@author: Administrator
'''

import tensorflow as tf


def variable_tt():
    x = tf.Variable([1, 2])
    a = tf.constant([2, 3])
    op_sub = a - x
    op_add = a + x
    
    # init
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        print(sess.run(op_sub))
        print(sess.run(op_add))

def constant_tt():
    a = tf.constant([1, 2], name="a", dtype=tf.float32)
    b = tf.constant([2.0, 3.0], name="b")
    c = a + b
    print(c)
    
    with tf.Session() as sess:
        result = sess.run(c)
        print(result)


if __name__ == '__main__':
#     import pdb; pdb.set_trace()
#     constant_tt()
    variable_tt()
