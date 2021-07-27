from lexer_config import Lexer
from parser_config import Parser

lxr = Lexer('in.txt')
prsr = Parser(lxr)

prsr.prog()
print(lxr.symbol_table)
