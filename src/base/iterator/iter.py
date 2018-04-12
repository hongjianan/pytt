# coding: UTF-8

from collections import Iterable


class NumIter:
    def __init__(self, start, end, distance = 1):
        self.start = start
        self.end = end
        self.distance = distance

    # python3中实现下面这两个方法的才是Iterator
    '''
    def __iter__(self):
        return self

    def __next__(self):
        if self.start + self.distance >= self.end:
            raise StopIteration
        value, self.start = self.start, self.start + self.distance
        return value
    '''

    def next(self):
        if self.start + self.distance >= self.end:
            raise StopIteration
        value, self.start = self.start, self.start + self.distance
        return value


def run():
    it = NumIter(0, 5)
    while True:
        try:
            print(next(it))
            print(it.next())
        except StopIteration as e:
            print("StopIteration", e)
            break

    print("===========")

    l = [1, 2, 3]
    i = iter(l)
    while True:
        try:
            print(next(i))
            print(i.next())
        except StopIteration as e:
            print("StopIteration", e)
            break

    for i in l:
        print(i)

    print("===========")

    print(isinstance('a', Iterable))

if __name__ == "__main__":
    run()
    

