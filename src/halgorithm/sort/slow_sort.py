# -*- coding: utf-8 -*-

import common


def insert_sort(data, cmp = common.less):
    ''' '''
    left = 1
    right = len(data) - 1
    while left <= right:
        idx = left - 1
        value = data[left]
        while idx >= 0 and cmp(value, data[idx]):
            data[idx + 1] = data[idx]
            idx -= 1
        if left != idx + 1:
            data[idx + 1] = value
        left += 1


def select_sort(data, cmp = common.less):
    ''' '''
    pop = common.min_index
    if cmp is common.greater:
        pop = common.max_index

    left = 0
    right = len(data) - 1
    while left < right:
        value, index = pop(data, left)
        if left != index:
            data[index], data[left] = data[left], value
        left += 1


def bubble_sort(data, cmp = common.less):
    ''''''
    right = len(data) - 1
    while right > 0:
        left = 0
        flag = False
        while left < right:
            if cmp(data[left + 1], data[left]):
                data[left], data[left + 1] = data[left + 1], data[left]
                flag = True
            left += 1
        if not flag:
            break
        right -= 1


def run():
    data = [2, 1, 3, 0, 2]

    insert_sort(data, common.less)
    # select_sort(data, common.less)
    # bubble_sort(data, common.less)

    print(data)


if __name__ == "__main__":
    run()

