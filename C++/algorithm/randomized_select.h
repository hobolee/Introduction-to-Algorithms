int randomized_select(double a[], int low, int high, int i) {
	if (low == high) {
		return a[low - 1];
	}

	int mid = partition(a, low, high);
	int k = mid - low + 1;
	if (i == k) {
		return a[mid - 1];
	}
	else if (i < k) {
		return randomized_select(a, low, mid - 1, i);
	}
	else {
		return randomized_select(a, mid + 1, high, i - k);
	}
}