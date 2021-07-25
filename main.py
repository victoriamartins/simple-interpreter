from lexer_config import Lexer
from token_config import TokenType
from parser_config import Parser

lxr = Lexer('in.txt') # verify negative numbers
prsr = Parser(lxr)

prsr.prog()
print(lxr.symbol_table)
