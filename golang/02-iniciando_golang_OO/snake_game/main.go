package main

import (
	"fmt"
	"time"

	"github.com/mramos90/snake-terminal-go/os_deps"
)

type Snake struct {
	X    int
	Y    int
	Char string
}

type Platform struct {
	Cols   int
	Lines  int
	Output [60][20]string
}

var plt = *NewPlatform(60, 20)

func NewPlatform(c int, l int) *Platform {
	return &Platform{
		Cols:  c,
		Lines: l,
	}
}

func (p *Platform) init_output() {

	for i, line := range p.Output {
		for j, _ := range line {
			p.Output[i][j] = "_"
			// col = "-"
		}
	}
	p.print_platform()
}

func (p *Platform) print_platform() {
	for i, line := range p.Output {
		for j, _ := range line {
			fmt.Printf("%s", p.Output[i][j])
		}
		fmt.Println()
	}
}

func (p *Platform) drawPlatform() {
	for i, line := range p.Output {
		for j, _ := range line {
			p.Output[i][j] = " "
			if i == 0 {
				p.Output[i][j] = "-"
			} else if i == 19 {
				p.Output[i][j] = "-"
			}
			if snake.X == i && snake.Y == j {
				p.Output[i][j] = snake.Char
			}
		}
	}
}

var snake = Snake{
	X:    0,
	Y:    0,
	Char: "#",
}

func UpdateGame() {
	for {
		os_deps.CallClear()
		snake.Y += 1
		snake.X += 1

		time.Sleep(1 * time.Microsecond)
		plt.drawPlatform()
		plt.print_platform()
	}
}

func main() {
	plt.init_output()
	UpdateGame()
}
