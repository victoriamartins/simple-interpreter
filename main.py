from lexer_config import Lexer
from token_config import TokenType
from parser_config import Parser

a = Lexer('in.txt')
'''
while True:
    b = a.next_token()
    print(f'{b.type}, {b.attribute}')
    if b.type == TokenType.Invalid:
        break
'''