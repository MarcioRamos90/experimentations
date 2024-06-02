package main

import "fmt"

func main() {
	x := 10

	fmt.Println(&x, x)

	y := &x

	fmt.Println(y, *y)

	*y = 10 + 10

	fmt.Println(x)

	var z *int = &x

	*z = 100

	fmt.Println(z, x)
}
