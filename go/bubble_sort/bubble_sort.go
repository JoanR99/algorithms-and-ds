package main

import "fmt"

func bubble_sort(array [5]int) [5]int {
	for i := 0; i < len(array); i++ {
		for j := 0; j < len(array)-1-i; j++ {
			if array[j] > array[j+1] {
				tmp := array[j]
				array[j] = array[j+1]
				array[j+1] = tmp
			}
		}
	}

	return array
}

func main() {
	a := [5]int{2, 4, 2, 8, 1}

	fmt.Println(bubble_sort(a))
}
