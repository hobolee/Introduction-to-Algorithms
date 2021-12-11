#pragma once
#include <list>
#include <tuple>

using namespace std;

// return tuple for returning multi values
tuple<double, int, int> find_max_sub_crossing(double a[], int low, int mid, int high) {
	// list for recording max
	std::list<double> res;
	res.push_back(a[mid] + a[mid + 1]);
	double res_max = res.back();
	int r = mid + 1;
	int l = mid;
	double tmp;
	for (int i = mid + 2; i <= high; i++) {
		tmp = res.back() + a[i];
		if (tmp > res_max) {
			res_max = tmp;
			r = i;
		}
		res.push_back(tmp);
	}

	res = { res_max };
	for (int i = mid - 1; i >= 0; i--) {
		tmp = res.back() + a[i];
		if (tmp > res_max) {
			res_max = tmp;
			l = i;
		}
		res.push_back(tmp);
	}
	return make_tuple(res_max, l, r);
}

tuple<double, int, int> find_max_sub(double a[], int low, int high) {
	if (low < high) {
		int mid = (low + high) / 2;
		auto res1 = find_max_sub(a, low, mid);
		auto res2 = find_max_sub(a, mid + 1, high);
		auto res3 = find_max_sub_crossing(a, low, mid, high);

		// cation: how to get values from tuple
		double re1 = get<0>(res1);
		double l1 = get<1>(res1);
		double r1 = get<2>(res1);
		double re2 = get<0>(res2);
		double l2 = get<1>(res2);
		double r2 = get<2>(res2);
		double re3 = get<0>(res3);
		double l3 = get<1>(res3);
		double r3 = get<2>(res3);
		// cannot find index
		// double res = (((res1>res2)?res1:res2)>res3)?((res1>res2)?res1:res2):res3;
		
		//try not to use multi-layers if
		if (re1 > re2 && re1 > re3) {
			return make_tuple(re1, l1, r1);
		}
		else if (re2 > re1 && re2 > re3) {
			return make_tuple(re2, l2, r2 );
		}
		else {
			return make_tuple(re3, l3, r3);
		}
	}
	else
	{
		return make_tuple(a[low], low, high);
	}

}

