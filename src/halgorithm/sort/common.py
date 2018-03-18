# coding: UTF-8


def greater(x, y):
    return x > y


def less(x, y):
    return x < y


def extreme_index(data, cmp, left, right):
    value = data[left]
    index = left
    left += 1
    while left < right:
        if cmp(data[left], value):
            value = data[left]
            index = left
        left += 1
    return value, index


def max_index(data, left = 0, right = -1):
    if -1 == right:
        right = len(data)
    return extreme_index(data, greater, left, right)


def min_index(data, left = 0, right = -1):
    if -1 == right:
        right = len(data)
    return extreme_index(data, less, left, right)


def run():
    pass


if __name__ == "__main__":
    run()
    

