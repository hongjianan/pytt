# -*- coding: utf-8 -*-

class Base:
    def base(self):
        print("Base->base")


class A0(Base):
    def a(self):
        print("A0->a")

    def abb(self):
        print("A0->abb")

    def aabb(self):
        print("A0->aabb")


class A1(A0):
    def a(self):
        print("A1->a")

    def aabb(self):
        print("A1->aabb")


class B0(Base):
    def b(self):
        print("B0->b")

    def abb(self):
        print("B0->abb")

    def aabb(self):
        print("B0->aabb")


class B1(B0):
    def b(self):
        print("B1->b")

    def abb(self):
        print("B1->abb")

    def aabb(self):
        print("B1->aabb")

    def base(self):
        print("B1->base")

    def ba(self):
        print("B1->ba")
        self.aabb()


class AB(A1, B1):
    pass

def run():
    ab = AB()
    ab.a()
    ab.b()
    ab.abb()
    ab.aabb()
    ab.base()   # if python3 print("B1->base"); if python2 print("Base->base")
    ab.ba()


if __name__ == "__main__":
    run()
