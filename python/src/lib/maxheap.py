class MaxHeap:
    def __init__(self, arr):
        self.a = arr[:]
        self.length = len(arr)
        self.heap_size = len(arr)

    def insert(self, key):
        a = a + [key]


    def build_max_heap(self):
        for i in range(int(self.heap_size / 2), 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        largest = i
        if self.left(i) and self.a[self.left(i) - 1] > self.a[largest - 1]:
            largest = self.left(i)
        if self.right(i) and self.a[self.right(i) - 1] > self.a[largest - 1]:
            largest = self.right(i)
        if largest != i:
            self.a[i - 1], self.a[largest - 1] = self.a[largest - 1], self.a[i - 1]
            self.max_heapify(largest)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(self.heap_size, 1, -1):
            self.a[0], self.a[i - 1] = self.a[i - 1], self.a[0]
            self.heap_size -= 1
            self.max_heapify(1)
        self.heap_size = len(self.a)
        return self.a

    def left(self, i):
        left_index = i * 2
        if left_index <= self.heap_size:
            return left_index
        else:
            return None

    def right(self, i):
        right_index = i * 2 + 1
        if right_index <= self.heap_size:
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
    a = [1, 2, 3]
    A = MaxHeap(a)
    b = A.heap_sort()
    print(b)
    pass
