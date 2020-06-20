// map
package main

import "fmt"

func main() {
	var mp map[string]int = map[string]int{
		"apple":  5,
		"pear":   6,
		"orange": 9,
	}

	fmt.Println(mp["apple"])
	delete(mp, "apple")
	// mp1 := make(map[string]int)

	val, ok := mp["orange"]
	print(val, ok)

}
