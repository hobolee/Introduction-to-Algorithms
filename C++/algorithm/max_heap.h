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
	void BuildMaxHeap();
	void MaxHeapify(int i);
	void HeapSort();
	int left(int i);
	int right(int i);
	int parent(int i);

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

void MaxHeap::BuildMaxHeap()
{
	for (int i = floor(heap_size / 2); i > 0; i--) {
		MaxHeap::MaxHeapify(i);
	}
}

void MaxHeap::MaxHeapify(int i)
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
		MaxHeapify(largest);
	}
}

void MaxHeap::HeapSort() {
	BuildMaxHeap();
	for (int i = heap_size; i > 1; i--) {
		int tmp = a[0];
		a[0] = a[i - 1];
		a[i - 1] = tmp;
		heap_size--;
		MaxHeapify(1);
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