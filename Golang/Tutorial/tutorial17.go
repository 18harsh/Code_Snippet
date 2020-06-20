package main

import "fmt"

func test() {
	fmt.Println("Hello")
}

func main() {
	x := test
	x()
}
