import sys, os, re

#expected form of a C program, without line breaks
source_re = r"int main\s*\(\s*\)\s*{\s*return\s+(?P<ret>[0-9]+)\s*;\s*}" 

# Use 'main' instead of '_main' if not on OS X
assembly_format = """    
    .globl _main
_main:
    movl    ${}, %eax
    ret
"""
from token_1 import TokenType

class Token():
    def __init__(self, type: TokenType, value = None) -> None:
        self.type = type
        self.value = value
    
    def __repr__(self) -> str:
        if self.value is None:
            return f"<{self.type}>"
        
        return f"<{self.type}: {self.value}>"

import re


class RegexEqual(str):
    def __eq__(self, pattern):
        return bool(re.search(pattern, self))

class Scanner():
    def __init__(self, source) -> None:
        self.source = source
        self.tokens  = []

    def scan(self):
        for w in self.source:
            match RegexEqual(w):
                case r'int':
                    self.tokens.append(Token(TokenType.INT_KEYWORD))
                case r'\(':
                    self.tokens.append(Token(TokenType.OPEN_PAREN))
                case r'\)':
                    self.tokens.append(Token(TokenType.CLOSE_PAREN))
                case r'{':
                    self.tokens.append(Token(TokenType.OPEN_BRACE))
                case r'}':
                    self.tokens.append(Token(TokenType.CLOSE_BRACE))
                case r';':
                    self.tokens.append(Token(TokenType.SEMICOLON))
                case r'return':
                    self.tokens.append(Token(TokenType.RETURN_KEYWORD))
                case r'[a-zA-Z]\w*':
                    self.tokens.append(Token(TokenType.IDENTIFIER, w))
                case r'[0-9]+':
                    self.tokens.append(Token(TokenType.INTEGER_LITERAL, w))
        return self.tokens
                

if __name__ == "__main__":

    source_file = sys.argv[1]
    print(source_file)
    assembly_file = os.path.splitext(source_file)[0] + ".s"

    with open(source_file, 'r') as infile, open(assembly_file, 'w') as outfile:
        source = infile.read().strip().split()
        print(Scanner(source).scan())
        # match = re.match(source_re, source)

        # extract the named "ret" group, containing the return value
        # retval = match.group('ret') 
        # outfile.write(assembly_format.format(retval))