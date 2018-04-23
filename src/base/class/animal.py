# coding: UTF-8

"""
public:
private: 只能本类中访问 __func(), __field
    除非使用 _class__field
"""

class HongType(type):
    def __init__(self, what, bases = None, dict = None):
        print("HongType __init__")
        super(HongType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("HongType __call__")
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj)


class Animal(object):
    # __metaclass__ = HongType  # 指定类创建器

    # static field
    count = 0

    # static method
    @staticmethod
    def get_count():
        return Animal.count

    # 类方法是静态方法的特殊版本，加了cls参数，可以将类的信息传入方法中
    @classmethod
    def class_name(cls):
        return cls.__name__

    def __init__(self):
        print("Animal __init__ self:%s" % self)
        Animal.count += 1
        self.__age = 0
        self.__weight = 0

    def __new__(cls, *args, **kwargs):
        print("Animal __new__")
        return object.__new__(cls, *args, **kwargs)

    def __del__(self):  # 相当于析构函数
        # print("Animal __del__ self:%s" % self)
        pass

    # obj()就会调用 __call__()
    def __call__(self):
        print("Animal __call__")

    # obj[key]就会调用 __getitem__()
    def __getitem__(self, item):
        print("Animal __getitem__", type(item), item)

    def __setitem__(self, key, value):
        print("Animal __setitem__", key, value)

    def __delitem__(self, key):
        print("Animal __delitem__", key)

    # python2: obj[1:3]   python3: __getitem__()
    def __getslice__(self, begin, end):
        print("Animal __getslice__", begin, end)

    # python2: obj[1:3]   python3: __setitem__()
    def __setslice__(self, begin, end):
        print("Animal __setslice__", begin, end)

    # python2: obj[1:3]   python3: __delitem__()
    def __delslice__(self, begin, end):
        print("Animal __delslice__", begin, end)

    def __iter__(self):
        print("Animal __iter__")
        yield 1
        yield 2

    def print_self(self):
        print(self)

    # 特性的函数不能有 self 之外的入参
    # obj.get_age() --> obj.get_age, 将method 伪造成 field
    @property
    def age(self):
        """获取field"""
        return self.__age

    # 使用__builtin__的 wrapper property之后，会生成另外一个 wrapper age.setter
    @age.setter
    def age(self, age):
        """设置field"""
        if not isinstance(age, int):
            raise ValueError('param age: must be int')
        if 0 > age or age > 150:
            raise ValueError('param age: must be in [0, 150]')
        self.__age = age

    def get_weight(self):
        return self.weight

    def get_age(self):
        return self.age

    def grow(self):
        self.age += 1

    def breathe(self):
        print("Animal breathe")

    def eat(self):
        self.weight += 1


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        # Animal.__init__(self)

    def say(self):
        print("Dog say wang")

    def get_age(self):
        # return self.__age     # Base private member can not access
        return self.age


def run():
    animal = Animal()
    print(Animal.__dict__)
    print(animal.__dict__)
    print("==============")

    print(Animal.get_count(), Animal.class_name())

    print(animal.age)
    animal.age = 10
    print(animal.age)
    # print(animal.__age)   # private
    # 访问 private
    print(animal._Animal__age)

    print("==========")
    dog = Dog()
    print(dog.get_age())

    print("====== call =======")
    dog()   # __call__()
    dog["item"] # __getitem__()
    dog["key"] = "value"
    del dog["key"]
    dog[1:3]

    for i in dog:   # __iter__
        print(i)



if __name__ == "__main__":
    run()
