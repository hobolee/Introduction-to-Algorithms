from math import floor


def find_max_sub(a, low, high):
    if low < high:
        mid = floor((low + high) / 2)
        res1, index_l_1, index_r_1 = find_max_sub(a, low, mid)
        res2, index_l_2, index_r_2 = find_max_sub(a, mid+1, high)
        res3, index_l_3, index_r_3 = find_max_sub_crossing(a, low, mid, high)
        res = [res1, res2, res3]
        # not __getitem__(), () means call, without () means itself
        index = max(range(len(res)), key=res.__getitem__)
        index_l = eval("index_l_%s" % str(index+1))
        index_r = eval("index_r_%s" % str(index+1))
        return max(res1, res2, res3), index_l, index_r
    else:
        return a[low], low, high


def find_max_sub_crossing(a, low, mid, high):
    # must have mid and mid+1 for the case of crossing mid
    # so it will be linear cost to traverse the array
    res = [a[mid] + a[mid + 1]]
    # find the max of the right part
    for i in range(mid+2, high+1):
        res.append(res[-1] + a[i])
    index_r = max(range(len(res)), key=res.__getitem__) + mid + 1
    res = [max(res)]
    # find the max fo whole part
    for i in range(mid-1, low-1, -1):
        res.append(res[-1] + a[i])
    index_l = mid - max(range(len(res)), key=res.__getitem__)
    return max(res), index_l, index_r

