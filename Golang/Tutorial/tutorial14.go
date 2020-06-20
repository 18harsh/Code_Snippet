// range
package main

import "fmt"

func main() {
	var a []int = []int{1, 3, 4, 56, 7, 8, 9, 2, 44, 78, 4}
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i])
	}
	for i, element := range a {
		for j, ele := range a {
			if ele == element && i < j {
				fmt.Println(element)
			}
		}
	}
}
