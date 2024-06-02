package main

import "fmt"

func main() {

	m := make(map[string]int)

	m["a"] = 10
	m["b"] = 90
	m["c"] = 90

	fmt.Println(m)

	delete(m, "c")

	fmt.Println(m)
	fmt.Println(m["c"])
	fmt.Println(m["x"])
	fmt.Println(m)

	_, c_exists := m["c"]
	_, a_exists := m["a"]

	fmt.Println(c_exists, a_exists)

	var map_x = map[string]int{"a": 123}
	fmt.Println(map_x)

	map_z := map[string]int{"hello": 90, "world": 60}
	fmt.Println(map_z)

	for _, k_verifier := range []string{"world", "xakira"} {
		if value, key_exists := map_z[k_verifier]; key_exists {
			fmt.Println("yes I do exist!", value)
		} else {
			fmt.Println("sorry, I am a trash.", k_verifier)
		}
	}
}
