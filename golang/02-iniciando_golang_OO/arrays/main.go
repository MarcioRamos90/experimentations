package main

import "fmt"

func main() {
	var x [10]int

	x[0] = 10
	x[2] = 90

	fmt.Printf("x: %v\n", x)
	fmt.Println(len(x))

	var y [10]string

	fmt.Println(y)

	z := [5]int{5, 4, 3, 3, 2}

	fmt.Println(z)
}
