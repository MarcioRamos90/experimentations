package main

import "fmt"

func twoReturns() (string, string) {
	return "Marcio", "Ramos"
}

func manyNums(n ...int) int {
	var res int
	for _, x := range n {
		res += x
	}
	return res
}

func funcInsindeOther() int {
	x := 10

	return func() int {
		x += 100
		return x
	}()
}

func funcInsindeOther2() func() int {
	x := 10

	return func() int {
		x += 100
		return x
	}
}

func main() {
	f := twoReturns
	fmt.Println(f())
	fmt.Println(twoReturns())
	fmt.Println(manyNums(1, 2, 3, 4, 5))

	z := 2

	addz := func() int {
		z += 3
		return z
	}

	fmt.Println(addz())

	fmt.Println(funcInsindeOther())
	fmt.Println(funcInsindeOther2()())
}
