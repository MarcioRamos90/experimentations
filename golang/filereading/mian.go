package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	TheIntireFile("thefile.txt")
	fmt.Println()
	TheFileLineByLine("thefile.txt")
	fmt.Println()
	TheFileWordByWord("thefile.txt")
}

func TheFileWordByWord(filename string) {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scan := bufio.NewScanner(f)
	scan.Split(bufio.ScanWords)
	count := 1

	for scan.Scan() {
		fmt.Println("word: ", count, " text: ", scan.Text())
		count++
	}

	if err := scan.Err(); err != nil {
		log.Fatal(err)
	}
}

func TheFileLineByLine(filename string) {
	f, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	scan := bufio.NewScanner(f)

	count := 1

	for scan.Scan() {
		fmt.Println("line: ", count, " text: ", scan.Text())
		count++
	}

	if err := scan.Err(); err != nil {
		log.Fatal(err)
	}
}

func TheIntireFile(filename string) {
	content, err := os.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
		return
	}
	fmt.Println(content)
	fmt.Println(string(content))
}
