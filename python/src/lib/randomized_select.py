from quick_sort import partition


def randomized_select(a, low, high, i):
    if low == high:
        return a[low - 1]
    mid = partition(a, low, high)
    k = mid - low + 1
    if i == k:
        return a[mid - 1]
    elif i < k:
        return randomized_select(a, low, mid - 1, i)
    else:
        return randomized_select(a, mid + 1, high, i - k)


if __name__ == "__main__":
    a = [1, 3, 2, 0, 5, 3, 7, 2, 9, 4, 6, 5, 11]
    b = randomized_select(a, 1, len(a), 4)
    print(b)
