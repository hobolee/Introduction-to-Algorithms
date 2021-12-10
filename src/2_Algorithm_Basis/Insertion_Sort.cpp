#include <iostream>

using namespace std;

void insert_sort(double a[], int len);

int main(){
    double d[] = {12.5, 15, 9, 20, 6, 31, 24 , 1, 5};
    // total memory size / single size -> length
    // error happens if calculate it in insert_sort, I guess it is related to the way to pass parameters.
    int length = sizeof(d) / sizeof(d[0]);
    insert_sort(d, length);
    // is there any way to output the array without for loop?
    cout << "Array after sorting is: " << endl;
    for (int i = 0; i < 9; i++){
        cout << d[i] << " ";
    }
    return 0;
}

void insert_sort(double a[], int len){
    // error
    // int length = sizeof(a) / sizeof(a[0]);
    for (int i = 1; i < len; i++){
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key){
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}