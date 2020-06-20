// Implicit vs Explicit
package main

import "fmt"

func main() {
	var number = 260
	num := 6
	var no uint64
	var bl bool

	fmt.Println(bl)
	fmt.Println(no)
	fmt.Printf("%T\n", num)
	fmt.Printf("%T", number)
}
