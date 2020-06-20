//print console and fmt
package main

import "fmt"

func main() {
	fmt.Printf("Hello %T %v\n", 10, 10)
	fmt.Printf("Hello %t", true)
	// var x string = fmt.Sprintf("Hello %T %v", 10, 10)
	fmt.Printf("Number: %.2f is cool", 3.455668889)
	fmt.Printf("Number: %07d is cool", 3)
}
