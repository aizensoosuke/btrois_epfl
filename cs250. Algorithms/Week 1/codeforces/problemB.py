#!/usr/bin/env python3

numbers_size = input()
numbers = [int(i) for i in input().split(" ")]

def merge_sort(a):
    def merge(l1, l2):
        infty = 100001
        l1.append(infty)
        l2.append(infty)
        return [l1.pop(0) if l1[0] < l2[0] else l2.pop(0) for i in range(len(l1) + len(l2) - 2)]

    if len(a) <= 1:
        return a
    else:
        middle = len(a) // 2
        left = a[:middle]
        right = a[middle:]
        return merge(merge_sort(left), merge_sort(right))

print(' '.join([str(i) for i in merge_sort(numbers)]))
