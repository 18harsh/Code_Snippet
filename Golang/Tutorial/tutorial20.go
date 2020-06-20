// struct
package main

import "fmt"

type Point struct {
	x int32
	y int32
}

type Circle struct {
	radius float64
	center *Point
}

func main() {
	p1 := &Point{y: 2}
	// var p2 Point = Point{-5, 7}
	c1 := Circle{4.56, p1}
	fmt.Println(c1.center.x)
}
