package parser

import (
    "strings"
    // /"fmt"
)

type Parser struct {
    Code string
    Curr string
    Right int
    Left int
}

func (p *Parser) AdvanceAll() {
    if p.Right < p.CodeLen() {
        p.Right++
        p.Left++
    }
}

func (p *Parser) AdvanceRight() {
    if p.Right < p.CodeLen() {
        p.Right++
    }
}


func (p *Parser) CodeLen() int {
    return int(len(p.Code))
}

func (p *Parser) GetCurr() string {
    return string(p.Code[p.Right])
}

func Parse(parser *Parser) []Token {
    var tokens = make([]Token, 0, parser.CodeLen())

    for parser.CodeLen() > parser.Right && parser.CodeLen() > parser.Left {
        cur := parser.GetCurr()
        switch {
        case ( 
            cur == "+" ||
            cur == "-" ||
            cur == "/" || 
            cur == "*"):
            tokens = append(tokens, Token{Type:MATH_OPERATOR, Value: cur})
            parser.AdvanceAll()
        case strings.Contains("1234567890", cur):
            tokens = append(tokens, Token{Type:IDENTIFIER, Value: cur})
            if strings.Contains(" \n\r\t", cur) {
                parser.Right++
                parser.Left = parser.Right
            } else {
                parser.AdvanceRight()
            }
        default:
            parser.AdvanceAll()
        }
    }

    return tokens
}

func ExecParser(code string) []Token {
    parser := Parser{Left: 0, Right: 0, Code: code}
    return Parse(&parser)
}
