package parser


// math
var MATH_OPERATOR = "MATH_OPERATOR"

// blocks
var PAREN_R = "PAREN_R"
var PAREN_L = "PAREN_L"

// indentifier
var IDENTIFIER = "IDENTIFIER"


type Token struct {
	Type string 
	Value string
}