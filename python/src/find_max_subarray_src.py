from lib.find_max_subarray import find_max_sub

a = [1, 3, 5.5, -4, 8, 3, 7]
# a = [1]
res, l, r = find_max_sub(a, 0, len(a)-1)
print("The max sub is: ", res, l, r)