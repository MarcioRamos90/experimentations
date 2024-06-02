package main

import (
	"fmt"
)

var b int = 22
var c, d string = "Hello", "World"

const (
	xcvb  int    = 1333
	qwe   string = "Hello, mothertruckers!"
	Afsdf string = "I am public!"
)

func main() {

	a := 10
	fmt.Printf("%v \n", a)
	fmt.Printf(("%v, %v %v\n"), c, d, b)

	fmt.Println()

	vars_func()

	// consts
	const xpto = xcvb - 10
	fmt.Printf("%v ::: %s ::: %s ::: %d", xcvb, qwe, Afsdf, xpto)

}

func vars_func() {
	a := 10
	b := "Hello"
	c := 12.909
	d := false
	e := 'W'
	f := `Waww`

	fmt.Printf("%v \n", a)
	fmt.Printf("%v \n", b)
	fmt.Printf("%v \n", c)
	fmt.Printf("%v \n", d)
	fmt.Printf("%v \n", e)
	fmt.Printf("%v \n", f)

}
