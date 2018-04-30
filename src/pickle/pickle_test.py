# -*- coding: utf-8 -*-

import pickle

class Person:
    def __init__(self, name, age = 0, weight = 0):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return "name={} age={} weight={}".format(self.name, self.age, self.weight)

    def growup(self):
        self.age += 1

    def eat(self):
        self.weight += 1


def pickle_tt():
    ming = Person("xiaoming")
    ming.growup()
    ming.eat()
    print(ming)

    pickle.dump(ming, open("record.log", "wb"))

    records = pickle.load(open('record.log'))
    print(records.name, records.age, records.weight)


def run():
    pickle_tt()


if __name__ == "__main__":
    run()
