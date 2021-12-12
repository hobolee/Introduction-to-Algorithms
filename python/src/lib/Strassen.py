from math import log2, floor


def strassen(a, b):
    l = int(len(a) / 2)
    if log2(len(a)) != floor(log2(len(a))) or log2(len(b)) != floor(log2(len(b))) \
            or log2(len(a[0])) != floor(log2(len(a[0]))) or log2(len(b[0])) != floor(log2(len(b[0]))) \
            or len(a) != len(a[0]) or len(b) != len(b[0]) or len(a) != len(b):
        print("The size of matrix is not suitable.")
        return
    if l < 1:
        return [[a[0][0] * b[0][0]]]

    s1 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(b[i][j + l] - b[i + l][j + l])
        s1.append(tmp)

    s2 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(a[i][j] + a[i][j + l])
        s2.append(tmp)

    s3 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(a[i + l][j] + a[i + l][j + l])
        s3.append(tmp)

    s4 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(b[i + l][j] - b[i][j])
        s4.append(tmp)

    s5 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(a[i][j] + a[i + l][j + l])
        s5.append(tmp)

    s6 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(b[i][j] + b[i + l][j + l])
        s6.append(tmp)

    s7 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(a[i][j + l] - a[i + l][j + l])
        s7.append(tmp)

    s8 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(b[i + l][j] + b[i + l][j + l])
        s8.append(tmp)

    s9 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(a[i][j] - a[i + l][j])
        s9.append(tmp)

    s0 = []
    for i in range(l):
        tmp = []
        for j in range(l):
            tmp.append(b[i][j] + b[i][j + l])
        s0.append(tmp)

    # to slice multiple dimension list is not essy
    a11 = []
    b11 = []
    for i in range(l):
        tmp_a = []
        tmp_b = []
        for j in range(l):
            tmp_a.append(a[i][j])
            tmp_b.append(b[i][j])
        a11.append(tmp_a)
        b11.append(tmp_b)

    a22 = []
    b22 = []
    for i in range(l):
        tmp_a = []
        tmp_b = []
        for j in range(l):
            tmp_a.append(a[i + l][j + l])
            tmp_b.append(b[i + l][j + l])
        a22.append(tmp_a)
        b22.append(tmp_b)

    p1 = strassen(a11, s1)
    p2 = strassen(s2, b22)
    p3 = strassen(s3, b11)
    p4 = strassen(a22, s4)
    p5 = strassen(s5, s6)
    p6 = strassen(s7, s8)
    p7 = strassen(s9, s0)

    c = []
    for i in range(l * 2):
        tmp = []
        for j in range(l * 2):
            if i < l and j < l:
                tmp.append(p5[i][j] + p4[i][j] - p2[i][j] + p6[i][j])
            # simplify if conditions
            elif i < l <= j:
                tmp.append(p1[i][j - l] + p2[i][j - l])
            elif j < l <= i:
                tmp.append(p3[i - l][j] + p4[i - l][j])
            else:
                tmp.append(p5[i - l][j - l] + p1[i - l][j - l] - p3[i - l][j - l] - p7[i - l][j - l])
        c.append(tmp)
    return c


if __name__ == "__main__":
    import numpy as np
    import time

    a1 = np.random.rand(64*2, 64*2)
    b1 = np.random.rand(64*2, 64*2)

    start = time.clock()
    # a*b means dot product, a.dot(b) means matrix product
    c1 = a1.dot(b1)
    print("time of numpy is: ", time.clock() - start)
    a2 = a1.tolist()
    b2 = b1.tolist()
    start = time.clock()
    c2 = strassen(a2, b2)
    print("time of mine is: ", time.clock() - start)
    c2 = np.array(c2)
    print('a', a1)
    print('b', b1)
    print('c1', c1)
    print('c2', c2)

    # sometimes accuracy is different
    print(c1 == c2)
