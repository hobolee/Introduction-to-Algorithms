#include <iostream>
#include "../include/insert_sort.h"
#include "../include/merge_sort.h"

using namespace std;

// void insert_sort(double a[], int len);

int main() {
	double d[] = { 12.5, 15, 9, 20, 6, 31, 24 , 1, 5 , 6, 7, 4};
	// total memory size / single size -> length
	// error happens if calculate it in insert_sort, I guess it is related to the way to pass parameters.
	int length = sizeof(d) / sizeof(d[0]);
	// insert_sort(d, length);
	merge_sort(d, 0, length - 1);
	// is there any way to output the array without for loop?
	cout << "Array after sorting is: " << endl;
	for (int i = 0; i < length; i++) {
		cout << d[i] << " ";
	}
	return 0;
}

