#include <iostream>
#include "insert_sort.h"
#include "merge_sort.h"
#include "find_max_subarray.h"
#include "max_heap.h"
#include "quick_sort.h"
#include "counting_sort.h"

using namespace std;

int main() {
	
	// double d[] = {12.5, 15, 9, 20, 6, 31, 24 , 1, 5 , 6, 7, 4, 3.3};
	int d[] = {1, 2, 3, 5, 7, 0, 2, 9, 5, 3, 3 };
	// total memory size / single size -> length
	// error happens if calculate it in insert_sort, i guess it is related to the way to pass parameters.
	int length = sizeof(d) / sizeof(d[0]);
	// insert_sort(d, length);
	// merge_sort(d, 0, length - 1);
	//quick_sort(d, 1, length);
	int * dd = counting_sort(d, 9, length);

	// is there any way to output the array without for loop?
	cout << "array after sorting is: " << endl;
	for (int i = 0; i < length; i++) {
	cout << dd[i] << " ";
	}
	delete dd;

	//double a[] = {1, 3, -5.5, -4, 8, 3, -7};
 //   int length = sizeof(a) / sizeof(a[0]);
 //   auto res = find_max_sub(a, 0, length - 1);
 //   cout << "The max sub is: " << get<0>(res) << " " << get<1>(res) << " " << get<2>(res) << endl;
	//return 0;

	/*MaxHeap mh;
	mh.append(1);
	mh.append(2);
	mh.append(3);
	mh.append(6);
	mh.append(5);
	cout << "Orignal a is: " << "a: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
	mh.heap_sort();
	cout << endl << "After heap sorting, a is: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}

	mh.build_max_heap();
	cout << endl << "After build, a is: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
	mh.extract_max();
	cout << endl << "After extract, a is: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
	mh.incrase_key(3, 100);
	cout << endl << "After increase, a is: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
	mh.insert(20);
	cout << endl << "After insert, a is: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}*/
}

