// switch
package main

import "fmt"

func main() {
	ans := 10
	switch ans {
	case 1:
		fmt.Println("one")
	case ans:
		fmt.Println("ten")
	default:
		fmt.Println("none")
	}
}
