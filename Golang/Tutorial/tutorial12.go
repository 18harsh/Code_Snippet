// Arrays
package main

import "fmt"

func main() {
	var arr [5]int
	arr[0] = 100
	fmt.Println(arr[0])

	// explicit
	arr1 := [3]int{4, 5, 6}
	fmt.Println(arr1)

	sum := 0
	for i := 0; i < len(arr1); i++ {
		sum += arr1[i]
	}
	fmt.Println(sum)

	arr2d := [2][3]int{{1, 2}, {3, 4}}
	fmt.Println(arr2d)
}
