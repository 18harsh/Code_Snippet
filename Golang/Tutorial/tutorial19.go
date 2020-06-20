// pointer
package main

import "fmt"

func changeValue(str *string) {
	*str = "changed!"
}

func changeValue2(str *string) {
	*str = "changed2!"
}

func main() {
	tochange := "hello"
	changeValue(&tochange)
	fmt.Println(tochange)
	changeValue2(&tochange)
	fmt.Println(tochange)
}
