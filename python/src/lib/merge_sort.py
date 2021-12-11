from math import floor


def merge(a, low, mid, high):
    tmp = []
    left = low
    right = mid+1
    while left <= mid and right <= high:
        if a[left] <= a[right]:
            tmp.append(a[left])
            left += 1
        else:
            tmp.append(a[right])
            right += 1
    if left <= mid:
        tmp = tmp + a[left:mid+1]
    if right <= high:
        tmp = tmp + a[right:high+1]
    a[low: high+1] = tmp[:]


def merge_sort(a, low, high):

    if low < high:
        mid = floor((low + high) / 2)
        merge_sort(a, low, mid)
        merge_sort(a, mid+1, high)
        merge(a, low, mid, high)


