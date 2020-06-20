// if else
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("Before if")
	scanner.Scan()
	var name = scanner.Text()
	if name == "harsh" {
		fmt.Println("inside if")
	} else if name == "HARSH" {
		fmt.Println("inside else if")
	} else {
		fmt.Println("inside else")
	}
	fmt.Println("After if")
}
