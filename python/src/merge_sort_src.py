from lib.merge_sort import merge_sort

a = [1, 3, 5.5, 4, 8, 3, 7]
print("Before sorting, array is: ", a)
merge_sort(a, 0, len(a)-1)
print("After sorting, array is: ", a)