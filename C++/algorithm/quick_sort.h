#include <random>


std::default_random_engine generator;


int partition(double a[], int low, int high) {
	std::uniform_int_distribution<int> distribution(low, high);
	int tmp_index = distribution(generator);
	double tmp = a[tmp_index - 1];
	a[tmp_index - 1] = a[high - 1];
	a[high - 1] = tmp;
	int i = low - 1;
	for (int j = low; j < high; j++) {
		if (a[j - 1] <= tmp) {
			i++;
			double tmp_low = a[i - 1];
			a[i - 1] = a[j - 1];
			a[j - 1] = tmp_low;
		}
	}
	a[high - 1] = a[i];
	a[i] = tmp;
	return i + 1;
}


void quick_sort(double a[], int low, int high) {
	if (low <= high) {
		int mid = partition(a, low, high);
		quick_sort(a, low, mid - 1);
		quick_sort(a, mid + 1, high);
	}
}
