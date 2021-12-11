#include <iostream>
#include "../include/find_max_subarray.h"

using namespace std;

int main(){
    double a[] = {1, 3};
    int length = sizeof(a) / sizeof(a[0]);
    auto [res, l, r] = find_max_sub(a, 0, length - 1);
    cout << "The max sub is: " << res << " " << l << " " << r << endl;
}