import random


def quick_sort(a, low, high):
    if low <= high:
        mid = partition(a, low, high)
        quick_sort(a, low, mid - 1)
        quick_sort(a, mid + 1, high)
        return a


def partition(a, low, high):
    tmp = random.randint(low, high)
    a[tmp - 1], a[high - 1] = a[high - 1], a[tmp - 1]
    tmp = a[high - 1]
    i = low - 1
    for j in range(low, high):
        if a[j - 1] <= tmp:
            i += 1
            a[j - 1], a[i - 1] = a[i - 1], a[j - 1]
    a[high - 1], a[i] = a[i], a[high - 1]
    return i + 1


if __name__ == "__main__":
    arr = [1, 3, 5, 3, 7, 2, 9, 4, 6, 5]
    quick_sort(arr, 1, len(arr))
    print(arr)
