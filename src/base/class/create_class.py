# coding: UTF-8


def type_tt():
    Foo = type("Foo", (), {'func': (lambda self, x: x * 2), 'func2': (lambda self, x: x * 3) })
    foo = Foo()
    print(foo.func(1))
    print(foo.func2(1))


def run():
    type_tt()


if __name__ == "__main__":
    run()
    

