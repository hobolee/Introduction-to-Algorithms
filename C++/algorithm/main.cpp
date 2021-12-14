#include <iostream>
#include "insert_sort.h"
#include "merge_sort.h"
#include "find_max_subarray.h"
#include "max_heap.h"

using namespace std;

int main() {
	
	//double d[] = { 12.5, 15, 9, 20, 6, 31, 24 , 1, 5 , 6, 7, 4};
	//// total memory size / single size -> length
	//// error happens if calculate it in insert_sort, i guess it is related to the way to pass parameters.
	//int length = sizeof(d) / sizeof(d[0]);
	//// insert_sort(d, length);
	//merge_sort(d, 0, length - 1);
	//// is there any way to output the array without for loop?
	//cout << "array after sorting is: " << endl;
	//for (int i = 0; i < length; i++) {
	//cout << d[i] << " ";
	//}

	//double a[] = {1, 3, -5.5, -4, 8, 3, -7};
 //   int length = sizeof(a) / sizeof(a[0]);
 //   auto res = find_max_sub(a, 0, length - 1);
 //   cout << "The max sub is: " << get<0>(res) << " " << get<1>(res) << " " << get<2>(res) << endl;
	//return 0;

	MaxHeap mh;
	mh.append(1);
	mh.append(2);
	mh.append(3);
	mh.append(6);
	mh.append(5);
	mh.append(4);
	mh.append(7);
	mh.append(9);
	mh.append(0);
	cout << "a: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
	mh.HeapSort();
	cout << endl << "a: ";
	for (int i = 0; i < mh.heap_size; i++) {
		cout << mh.a[i] << " ";
	}
}

