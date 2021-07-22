from lexer_config import Lexer
from token_config import TokenType
from parser_config import Parser

lxr = Lexer('in.txt')
prsr = Parser(lxr)

prsr.prog()

print(prsr.lexer.symbol_table)
'''
$x = 120 - 2 + 2/5;
$z = $x * 5;
print($z);
'''
