class MaxHeap:
    def __init__(self, arr):
        self.a = arr[:]
        self.length = len(arr)
        self.heap_size = len(arr)

    def build_max_heap(self):
        for i in range(int(self.heap_size / 2) - 1, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        largest = i
        if self.left(i) and self.a[self.left(i)] > self.a[largest]:
            largest = self.left(i)
        if self.right(i) and self.a[self.right(i)] > self.a[largest]:
            largest = self.right(i)
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.max_heapify(largest)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heap_size - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = len(self.a)
        return self.a

    def left(self, i):
        left_index = i * 2
        if left_index < self.heap_size:
            return left_index
        else:
            return None

    def right(self, i):
        right_index = i * 2 + 1
        if right_index < self.heap_size:
            return right_index
        else:
            return None

    def parent(self, i):
        if i > 0:
            parent_index = int(i / 2)
            return parent_index
        else:
            return None


if __name__ == "__main__":
    a = [1, 7, 2, 3, 5, 8, 4, 5]
    A = MaxHeap(a)
    b = A.heap_sort()
    print(b)
    pass

