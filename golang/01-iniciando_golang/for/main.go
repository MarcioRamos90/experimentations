package main

import "fmt"

func main() {

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	x := 0

	for x < 10 {
		fmt.Println(x)
		x++
	}

	c := 0
	for {
		c += 10
		fmt.Println(c)
		if c == 100 {
			break
		}
	}
}
