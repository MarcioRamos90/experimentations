package main

import "fmt"

func main() {
	n := 123
	slice := make([]int, 2, 5)
	fmt.Println(slice)
	slice = append(slice, n, 222, 333)
	n++
	slice = append(slice, n)
	n++
	slice = append(slice, n)
	n++
	slice = append(slice, n)
	fmt.Println(slice)
	fmt.Println(len(slice))
	fmt.Println(cap(slice))

	sliceStr := []string{
		"hello",
		"mamacita",
		"mothafocka",
	}

	fmt.Println(sliceStr[2:])
}
