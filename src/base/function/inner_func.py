# -*- coding: utf-8 -*-

class Foo:
    def __repr__(self):
        return "This is Foo"


def tt_1():

    # python3 才有的
    foo = Foo()
    print(ascii(list()))


def string_tt():
    name = "张三"
    byte_name = bytes(name)
    byte_array_name = bytearray(name)
    print(type(byte_name), byte_name)
    print(type(byte_array_name), byte_array_name)

    for i,byte in enumerate(byte_array_name):
        print(i, type(byte), byte)

    print(chr(97), ord('a'))


# def compile_tt():
#     namespace = {"name" : "hongjianan", "age" : 27}
#     code = 'print("test compile")'
#     func = compile(code, '<string>', 'exec')
#     exec func in namespace
#
#     result = namespace

def number_tt():
    print(pow(2, 4))
    print(bin(10), oct(10), int(10), hex(10))
    print(round(3.3), round(3.5))
    print(divmod(4, 3))
    print(sum([1, 2]))

    # eval有返回值
    expression = "(1 + 2) * 3"
    print("%s = %d" % (expression, eval(expression)))

    expression = "a * 3"
    print("%s = %d" % (expression, eval(expression, {"a" : 3})))

    print(hash(expression))


def exec_tt():
    statement = \
'''
for i in range(5):
    print(i)
'''
    # exec 没有返回值，用来执行代码
    # compile 用来编译代码
    exec(statement)


def attr_tt():
    '''
    反射：hasattr(), setattr(), getattr(), delattr()
    '''
    pass


def filter_tt():
    def positive(x):
        return x >= 0

    print(filter((lambda x: True if x >= 0 else False), [1, 0, -1, -2]))
    print(filter(positive, [1, 0, -1, -2]))
    # print(filter(positive, 1))   # error, arg2 must be iterable

    num = [1, 2, 3, 4]
    print([(x + 100) for x in num])
    print(map(lambda x: x + 100, num))


def iter_tt():
    # range will generator list data in memory, if range too big to memory error
    '''
    for i in range(1000 * 1000 * 1000):
        if i % (1000 * 1000) == 0:
            print(i)
    '''
    pass


def scope_tt():
    print(globals())

    print(locals())
    num = 1
    print(locals())


def type_tt():
    class MyList(list):
        pass

    print(isinstance([], list))
    print(isinstance({}, list))
    print(isinstance(MyList(), list))


def repr_tt():
    print(repr(list))


def slice_tt():
    # list __slice__()
    pass


def import_tt():
    import random as t
    print(t.uniform(0, 10))

    tt = __import__("random")
    print(tt.uniform(0, 10))


def run():
    # tt_1()
    # string_tt()
    # number_tt()
    # exec_tt()
    # filter_tt()
    # iter_tt()
    # scope_tt()
    # type_tt()
    # repr_tt()
    # slice_tt()
    import_tt()

if __name__ == "__main__":
    run()
    

