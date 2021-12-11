#include <list>

struct result
{
    double res; int l; int r;
};

result find_max_sub_crossing(double a[], int low, int mid, int high){
    std::list<double> res;
    res.push_back(a[mid] + a[mid + 1]);
    double res_max = res.back();
    int r = mid + 1;
    int l = mid;
    double tmp;
    for(int i = mid+2; i <= high; i++){
        tmp = res.back() + a[i];
        if(tmp > res_max){
            res_max = tmp;
            r = i;
        }
        res.push_back(tmp);
    }
    res = {res_max};
    for(int i = mid-1; i >= 0; i--){
        tmp = res.back() + a[i];
        if(tmp > res_max){
            res_max = tmp;
            l = i;
        }
        res.push_back(tmp);
    }
    return {res_max, l, r};
}

result find_max_sub(double a[], int low, int high){
    if(low < high){
        int mid = (low + high) / 2;
        auto [res1, l1, r1] = find_max_sub(a, low, mid);
        auto [res2, l2, r2] = find_max_sub(a, mid+1, high);
        auto [res3, l3, r3] = find_max_sub_crossing(a, low, mid, high);
        // cannot find index
        // double res = (((res1>res2)?res1:res2)>res3)?((res1>res2)?res1:res2):res3;
        if(res1 > res2 && res1 > res3){
            return {res1, l1, r1};
        }
        else if(res2 > res1 && res2 > res3){
            return {res2, l2, r2};
        }
        else{
            //return {res3, l3, r3};
        }
    }
    else
    {
        return {a[low], low, high};
    }
    
}

