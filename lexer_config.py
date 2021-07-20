from token_config import Token, TokenType


class Lexer:
    def __init__(self, file_in):
        self.position = -1
        source = open(file_in, 'r').readlines()
        self.input = str()
        self.symbol_table = dict()
        for i in source:
            for j in i:
                if j != '\n' and j != '\t' and j != ' ':
                    self.input = self.input + j

    def next_char(self):
        if self.position < len(self.input)-1:
            self.position += 1
            return self.input[self.position]
        return ' '

    def next_token(self):
        peek = self.next_char()
        if peek == '(':
            return Token(TokenType.Open)
        elif peek == ')':
            return Token(TokenType.Close)
        elif peek == ';':
            return Token(TokenType.Eol)
        elif peek == '=':
            return Token(TokenType.Eq)
        elif peek == '+':
            return Token(TokenType.Sum, '+')
        elif peek == '-':
            return Token(TokenType.Sub, '-')
        elif peek == '*':
            return Token(TokenType.Mult, '*')
        elif peek == '/':
            return Token(TokenType.Div, '/')
        elif peek.isnumeric():
            num = str()
            while True:
                num = num + peek
                peek = self.next_char()
                if not peek.isnumeric() and peek != '.':
                    self.position -= 1
                    break
            return Token(TokenType.Num, num)
        elif peek == '$':
            var = str()
            while True:
                var = var + peek
                peek = self.next_char()
                if not peek.isalnum():
                    self.position -= 1
                    break
            self.symbol_table[var] = False
            return Token(TokenType.Var, var)
        elif peek == 'p':
            command = str()
            while True:
                command = command + peek
                peek = self.next_char()
                if peek == '(':
                    self.position -= 1
                    break
            return Token(TokenType.Print)
        else:
            return Token(TokenType.Invalid)
