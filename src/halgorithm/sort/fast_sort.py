# coding: UTF-8


def quick_sort(data, left, right):
    if left >= right:
        return
    l = left
    r = right
    guard = data[left]

    while left < right:
        while left < right and data[right] > guard:
            right -= 1
        if left < right:
            data[left] = data[right]
            left += 1

        while left < right and data[left] < guard:
            left += 1
        if left < right:
            data[right] = data[left]
            right -= 1

    data[left] = guard
    quick_sort(data, l, left - 1)
    quick_sort(data, left + 1, r)


def merge_data(data, left, mid, right):
    print(data, left, right)
    tmp = []
    l = left; r = mid + 1
    while l <= mid and r <=right:
        if data[l] < data[r]:
            tmp.append(data[l])
            l += 1
        else:
            tmp.append(data[r])
            r += 1

    for i in xrange(l, mid + 1):
        tmp.append(data[i])

    for i in xrange(r, right + 1):
        tmp.append(data[i])

    for i in xrange(right - left + 1):
        data[left + i] = tmp[i]


def merge_sort(data, left, right):
    if left == right:
        return
    mid = (left + right) / 2
    merge_sort(data, left, mid)
    merge_sort(data, mid + 1, right)
    merge_data(data, left, mid, right)


# def heap_sort(data):
#     # init heap
#     size = len(data)




def run():
    data = [2, 1, 3, 0, 2]

    # shell_sort(data, common.less)
    # quick_sort(data, 0, len(data) - 1)
    # merge_sort(data, 0, len(data) - 1)
    # heap_sort(data, 0, len(data) - 1)

    print(data)


if __name__ == "__main__":
    run()
    

