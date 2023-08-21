package algorithm

import (
	"fmt"
	"math"
)

func binary_search(array [4]int, v int) bool {
	lo := 0
	hi := len(array)

	for lo < hi {
		m := int(math.Floor(float64(lo + (hi-lo)/2)))

		if array[m] == v {
			return true
		} else if array[m] > v {
			hi = m
		} else {
			lo = m + 1
		}
	}

	return false
}

func main() {
	a := [4]int{2, 4, 5, 8}

	fmt.Println(binary_search(a, 5))
	fmt.Println(binary_search(a, 6))
}
