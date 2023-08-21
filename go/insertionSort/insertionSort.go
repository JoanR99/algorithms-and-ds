package main

import "fmt"

func main() {
	a := [6]int{31, 41, 59, 26, 41, 58}

	for i := 1; i < len(a); i++ {
		key := a[i]
		j := i - 1

		for j >= 0 && a[j] > key {
			a[j+1] = a[j]
			j--
		}

		a[j+1] = key
	}

	for _, value := range a {
		fmt.Println(value)
	}
}
