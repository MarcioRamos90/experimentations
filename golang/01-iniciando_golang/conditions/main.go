package main

import "fmt"

func main() {
	a := 9
	if a >= 10 {
		fmt.Println(a)
	} else if a == 8 {
		fmt.Println("OK")
	} else {
		fmt.Println("Not OK")
	}

	b := true

	if x := "Cool"; b {
		fmt.Printf("Ok that's %s", x)
	}
}
