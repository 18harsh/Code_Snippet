// boolean exp
// logical exp:"!,&&,||"
package main

import "fmt"

func main() {
	x := 5
	y := 6.4
	val := float64(x)+1.4 != y || 7 < 9
	fmt.Printf("%t", val)
}
