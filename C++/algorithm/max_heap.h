#include <math.h>
#include <vector>

class MaxHeap
{
public:
	//std::list<int> a;	
	std::vector<int> a;
	int length;
	int heap_size = 0;
	void append(int i);
	void pop();
	void build_max_heap();
	void max_heapify(int i);
	void heap_sort();
	int left(int i);
	int right(int i);
	int parent(int i);
	int extract_max();
	void incrase_key(int i, int key);
	void insert(int key);

private:

};

void MaxHeap::append(int i)
{
	a.push_back(i);
	heap_size++;
	length = heap_size;
}

void MaxHeap::pop()
{
	a.pop_back();
	heap_size--;
	length = heap_size;
}

void MaxHeap::insert(int key) {
	heap_size++;
	length = heap_size;
	a[heap_size - 1] = INT_MIN;
	incrase_key(heap_size, key);
}

void MaxHeap::incrase_key(int i, int key) {
	if (key <= a[i - 1]) {
		cout << "Key is smaller than original value." << endl;
		exit(-1);
	}
	a[i - 1] = key;
	while (i > 1 && a[parent(i) - 1] < a[i - 1]) {
		int tmp = a[i - 1];
		a[i - 1] = a[parent(i) - 1];
		a[parent(i) - 1] = tmp;
		i = parent(i);
	}
}

int MaxHeap::extract_max() {
	if (heap_size < 1) {
		cout << "heap underflow" << endl;
		exit(-1);
	}
	int max = a[0];
	a[0] = a[heap_size - 1];
	heap_size--;
	length = heap_size;
	max_heapify(1);
	return max;
}

void MaxHeap::build_max_heap()
{
	for (int i = floor(heap_size / 2); i > 0; i--) {
		MaxHeap::max_heapify(i);
	}
}

void MaxHeap::max_heapify(int i)
{
	int largest = i;
	int aa = left(i);
	int bb = right(i);
		if (left(i) and a[left(i) - 1] > a[largest - 1]) {
		largest = left(i);
	}
	if (right(i) and a[right(i) - 1] > a[largest - 1]) {
		largest = right(i);
	}
	if (largest != i) {
		int tmp = a[largest - 1];
		a[largest - 1] = a[i - 1];
		a[i - 1] = tmp;
		max_heapify(largest);
	}
}

void MaxHeap::heap_sort() {
	build_max_heap();
	for (int i = heap_size; i > 1; i--) {
		int tmp = a[0];
		a[0] = a[i - 1];
		a[i - 1] = tmp;
		heap_size--;
		max_heapify(1);
	}
	heap_size = length;
}

int MaxHeap::left(int i) {
	int left_index = i * 2;
	if (left_index <= heap_size) {
		return left_index;
	}
	else{
		return NULL;
	}
}

int MaxHeap::right(int i) {
	int right_index = i * 2 + 1;
	if (right_index <= heap_size) {
		return right_index;
	}
	else {
		return NULL;
	}
}

int MaxHeap::parent(int i) {
	if (i > 0) {
		return floor(i / 2);
	}
	else {
		return NULL;
	}
}

