void merge(double a[], int low, int mid, int high){
    int left = low;
    int right = mid + 1;
    int i = 0;
    int len = high - low + 1;
    double* tmp = new double[len];
    while(left <= mid &&  right <= high){
        tmp[i++] = a[left] <= a[right] ? a[left++] : a[right++];
    }
    while(left <= mid){
        tmp[i++] = a[left++];
    }
    while (right <= high){
        tmp[i++] = a[right++];
    }
    for(int j = 0; j < len; ++j){
        a[low + j] = tmp[j];
    }
    delete [] tmp;
}

void merge_sort(double a[], int low, int high){
    if(low < high){
        int mid = (low + high) / 2;
        merge_sort(a, low, mid);
        merge_sort(a, mid+1, high);
        merge(a, low, mid, high);
    }
}