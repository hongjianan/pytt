# coding: UTF-8

import copy


def copy_tt():
    # number
    n1 = 1
    n2 = n1
    print(id(n1), id(n2))

    n2 = copy.copy(n1)
    n3 = copy.deepcopy(n1)
    print(id(n1), id(n2), id(n3))

    # string
    s1 = "abc"
    s2 = s1
    print(id(s1), id(s2))

    s2 = copy.copy(s1)
    s3 = copy.deepcopy(s1)
    print(id(s1), id(s2), id(s3))

    # list
    l1 = [1, 2, 3]
    l2 = l1
    print(id(l1), id(l2))

    l2 = copy.copy(l1)
    print(id(l1), id(l2))


def deepcopy_tt():
    ll1 = [[1, "a"]]
    ll2 = ll1
    ll3 = copy.copy(ll1)
    ll4 = copy.deepcopy(ll1)
    print(id(ll1), id(ll2), id(ll3), id(ll4))
    print(id(ll1[0]), id(ll2[0]), id(ll3[0]), id(ll4[0]))


def run():
    # copy_tt()
    deepcopy_tt()

if __name__ == "__main__":
    run()
