# coding: UTF-8

import sys


class Plant():
    def __init__(self):
        print("Plant __init__ self:%s" % self)

    def __del__(self):  # 相当于析构函数
        print("Plant __del__ self:%s" % self)

    def print_self(self):
        print(self)


class Animal(object):
    def __init__(self):
        print("Animal __init__ self:%s" % self)
        self.age = 0

    def __del__(self):  # 相当于析构函数
        print("Animal __del__ self:%s" % self)
        pass

    def print_self(self):
        print(self)

    def breathe(self):
        print("Animal breathe")


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()

    def breathe(self):
        print("Dog breathe")


def type_tt():
    animal = Animal()
    plant = Plant()
    print(type(Animal), type(animal))
    print(type(Plant), type(plant))


def del_tt():
    plant = Plant()
    print(plant)
    plant.print_self()
    del plant


def inherit_tt():
    dog = Dog()
    dog.breathe()


def member_tt():
    print(Animal.__dict__)
    print(Dog.__dict__)

    print("==============")

    dog = Dog()
    print(dog.__dict__)


def reflect_tt():
    print(hasattr(Dog, "age"), hasattr(Dog, "print_self"))
    print(hasattr(Dog(), "age"), hasattr(Dog(), "print_self"))


def run():
    # type_tt()
    # del_tt()
    # inherit_tt()
    # member_tt()
    reflect_tt()


if __name__ == "__main__":
    run()
