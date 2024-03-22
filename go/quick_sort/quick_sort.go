package main

import "fmt"

func partition(arr []int, lo int, hi int) int {
	pivot := arr[hi]
	idx := lo - 1

	for i := lo; i < hi; i++ {
		if arr[i] <= pivot {
			idx++
			tmp := arr[i]
			arr[i] = arr[idx]
			arr[idx] = tmp
		}
	}

	idx++

	arr[hi] = arr[idx]
	arr[idx] = pivot

	return idx
}

func quickSort(arr []int, lo int, hi int) {
	if lo >= hi {
		return
	}

	pivotIdx := partition(arr, lo, hi)

	quickSort(arr, lo, pivotIdx-1)
	quickSort(arr, pivotIdx+1, hi)
}

func main() {
	arrTest := []int{8, 6, 2, 3, 9}
	quickSort(arrTest, 0, len(arrTest)-1)
	fmt.Println(arrTest)
}
