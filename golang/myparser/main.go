package main

import (
    "fmt"
    "myparser/parser"
    "myparser/tree"
)

func main() {
	var str string = "4 / 3 * 2 + 5 * 3" 
    tokens := parser.ExecParser(str)    
    fmt.Println("Tokenizer -> ", tokens)
    tree.StartTree(tokens) 
}

