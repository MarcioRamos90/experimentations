package main

import (
	"encoding/json"
	"fmt"
)

type Car struct {
	Name  string
	Year  int
	color string
}

func (c Car) josnFy() ([]byte, error) {
	res, err := json.Marshal(c)
	if err != nil {
		return nil, err
	}
	fmt.Printf("%s\n", res)
	return res, nil
}

func main() {
	car := Car{"Gol", 2017, "Vermelho"}

	res, err := json.Marshal(car)

	if err != nil {
		fmt.Println("Error to serialize:", err)
	}

	fmt.Printf("%s\n", res)

	carbytes, err := car.josnFy()
	fmt.Println(string(carbytes))
}
