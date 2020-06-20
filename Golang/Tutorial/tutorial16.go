// functions
package main

import "fmt"

func test(x, y int) (int, int) {
	defer fmt.Println("func completed")
	fmt.Println("before return")
	return x + y, x - y

}

func main() {
	ans1, ans2 := test(5, 6)
	fmt.Println(ans1, ans2)
}
