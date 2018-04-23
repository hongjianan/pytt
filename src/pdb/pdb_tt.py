
def add(a, b):
    return a + b


def calc(a, b):
    import pdb
    pdb.set_trace()
    c = utils.add(a, b)
    print(c)


if __name__ == '__main__':
    calc(1, 2)
