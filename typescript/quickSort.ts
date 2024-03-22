function partition(arr: number[], lo: number, hi: number): number {
	const pivot = arr[hi];
	let idx = lo - 1;

	for (let i = lo; i < hi; i++) {
		if (arr[i] <= pivot) {
			idx++;
			const tmp = arr[i];
			arr[i] = arr[idx];
			arr[idx] = tmp;
		}
	}

	idx++;

	arr[hi] = arr[idx];
	arr[idx] = pivot;

	return idx;
}

function quickSort(arr: number[], lo: number, hi: number): void {
	if (lo >= hi) {
		return;
	}

	const pivotIdx = partition(arr, lo, hi);

	quickSort(arr, lo, pivotIdx - 1);
	quickSort(arr, pivotIdx + 1, hi);
}

const arrTest = [3, 2, 1, 5, 6, 4];

quickSort(arrTest, 0, arrTest.length - 1);

console.log(arrTest);
