package tree

import (
	"fmt"
	"myparser/parser"
)


type BinTree struct {
	Left *BinTree
	Value string
	Right *BinTree
	Parent *BinTree
}

func PrintBinaryTree(b * BinTree) {
	if b == nil {
		return
	}
	fmt.Print("(")
	PrintBinaryTree(b.Left)
	
	fmt.Print(b.Value)

	PrintBinaryTree(b.Right)
	fmt.Print(")")
	
}

func AddChildren(bParent, bChildren *BinTree) *BinTree {
	if bChildren.Parent != nil {
		return AddChildren(bParent, bChildren.Parent)
	}
	
	bChildren.Parent = bParent

	if bParent.Left == nil {
		bParent.Left = bChildren
	} else if bParent.Right == nil {
		bParent.Right = bChildren
	}

	return bParent
}

func IsPlusOrMinus(operator string) bool {
	return operator == "+" || operator == "-"
}


func IsMultOrDiv(operator string) bool {
	return operator == "*" || operator == "/"
}

func FindNextOperator(tokens []parser.Token, cur int) int {
	for idx, t := range(tokens) {
		if IsPlusOrMinus(t.Value) && idx > cur {
			return idx
		} else if IsMultOrDiv(t.Value) && idx > cur {
			return idx
		}
	}
	return -1
}

func GetMostParent(b * BinTree) * BinTree {
	if (b.Parent == nil) {
		return b
	}
	return GetMostParent(b.Parent)
} 

func HandleBinTree(b * BinTree, tokens []parser.Token, lastTokensOperatorsIndexes []int, cur int) {
	if cur >= len(tokens) {
		return
	}

	if cur == -1 {
		return
	}

	lastTokenIdx := len(lastTokensOperatorsIndexes) - 1

	if len(lastTokensOperatorsIndexes) > 0 {
		if IsPlusOrMinus(tokens[cur].Value) {
			b = AddChildren(&BinTree{Value: tokens[cur].Value}, b)
			b = AddChildren(b, &BinTree{Value: tokens[cur + 1].Value})
		}
		if IsMultOrDiv(tokens[cur].Value) && IsPlusOrMinus(tokens[lastTokensOperatorsIndexes[lastTokenIdx]].Value) {
			b = b.Right
			temp := b.Value
			b.Value = tokens[cur].Value
			b = AddChildren(b, &BinTree{Value: temp})
			b = AddChildren(b, &BinTree{Value: tokens[cur + 1].Value})
		} else if IsMultOrDiv(tokens[cur].Value) && IsMultOrDiv(tokens[lastTokensOperatorsIndexes[lastTokenIdx]].Value) {
			b = AddChildren(&BinTree{Value: tokens[cur].Value}, b)
			b = AddChildren(b, &BinTree{Value: tokens[cur + 1].Value})
		}
		lastTokensOperatorsIndexes = append(lastTokensOperatorsIndexes, cur)
	} else {
		if IsPlusOrMinus(tokens[cur].Value) || IsMultOrDiv(tokens[cur].Value) {
			b.Value = tokens[cur].Value
			b = AddChildren(b, &BinTree{Value: tokens[cur - 1].Value})
			b = AddChildren(b, &BinTree{Value: tokens[cur + 1].Value})
			} else if tokens[cur].Value == "(" || tokens[cur].Value == ")" {
			}
		lastTokensOperatorsIndexes = append(lastTokensOperatorsIndexes, cur)
	}
	next := FindNextOperator(tokens, cur)
	if next > -1 {
		HandleBinTree(b, tokens, lastTokensOperatorsIndexes, next)
	}
}

func StartTree(tokens []parser.Token) {
	b := BinTree{}
	l := make([]int, 0, len(tokens))
	cur := FindNextOperator(tokens, 0)
	HandleBinTree(&b, tokens, l, cur)
	res := GetMostParent(&b)
	PrintBinaryTree(res)
	fmt.Println()
	fmt.Println(res)
}
