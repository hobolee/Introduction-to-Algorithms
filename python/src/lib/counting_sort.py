def counting_sort(a, k):
    c = [0] * (k + 1)
    b = [None] * len(a)
    for i in range(len(a)):
        c[a[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for i in range(len(a) - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1

    return b


if __name__ == "__main__":
    a = [1, 3, 0, 5, 3, 7, 2, 9, 4, 6, 5, 11]
    b = counting_sort(a, 11)
    print(b)
