package main

import "fmt"

type Student struct {
	name   string
	grades []int
	age    int
}

// func (s *Student) getAge(age int) {
// 	s.age = age
// }

func (s Student) getaveGrade() float32 {
	sum := 0
	for _, v := range s.grades {
		sum += v
	}
	return float32(sum) / float32(len(s.grades))
}

func main() {
	s1 := Student{"harsh", []int{70, 90, 80, 85}, 19}
	average := s1.getaveGrade()
	fmt.Println(average)
}
