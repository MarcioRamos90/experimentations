package main

import "fmt"

type Car struct {
	Name        string
	Yer         int
	Color       string
	IsAutomatic bool
}

type SuperCar struct {
	Car
	CanFly bool
}

func (c Car) info() string {
	return fmt.Sprintf("The model is %s,\nmake in %d, \ncolor is %s, \nis automatic %v\n", c.Name, c.Yer, c.Color, c.IsAutomatic)
}

func main() {
	car1 := Car{
		Name:        "Corrolla",
		Yer:         2016,
		Color:       "Preto",
		IsAutomatic: true,
	}

	car2 := Car{"Celta", 2010, "Preto", false}

	fmt.Println(car1.info())
	fmt.Println(car2.info())

	scar1 := SuperCar{Car{"Tesla", 2023, "Prata", true}, true}

	fmt.Println(scar1.Name, scar1.CanFly, scar1.Yer)
	fmt.Println(scar1.info())
}
