from token_config import Token, TokenType


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.next_token()
        self.output = str()

    def prog(self):
        self.stmt()
        self.match(self.lookahead)
        self.lines()

    def lines(self):
        if self.lookahead.type != TokenType.Invalid:
            self.prog()

    def stmt(self):
        if self.lookahead.type == TokenType.Var:
            self.atr()
        elif self.lookahead.type == TokenType.Print:
            self.imp()
        else:
            print('Syntax error: Var or print were expected.')

    def imp(self):
        self.match(self.lookahead)  # print
        self.match(self.lookahead)  # open
        ref = self.lookahead.attribute
        if ref in self.lexer.symbol_table:
            value = self.lexer.symbol_table[ref]
            print(value)
        else:
            print(f'Symbol {self.lookahead.attribute} is not defined.')
        self.match(self.lookahead)  # var
        self.match(self.lookahead)  # close

    def atr(self):
        ref = self.lookahead.attribute  # it gets the name
        self.match(self.lookahead)  # it matches VAR
        self.match(self.lookahead)  # it matches EQ
        result_expr = self.expr()
        self.lexer.symbol_table[ref] = result_expr

    def expr(self):
        result_fact = self.fact()
        if self.lookahead.type == TokenType.Sum:
            self.match(self.lookahead)  # it matches SUM
            result_expr = self.expr()
            return result_fact + result_expr
        elif self.lookahead.type == TokenType.Sub:
            self.match(self.lookahead)  # it matches SUB
            result_expr = self.expr()
            return result_fact - result_expr
        else:
            return result_fact

    def fact(self):
        result_term = self.term()  # number
        if self.lookahead.type == TokenType.Mult:
            self.match(self.lookahead)  # it matches MULT
            result_fact = self.fact()
            return result_term * result_fact
        elif self.lookahead.type == TokenType.Div:
            self.match(self.lookahead)  # it matches DIV
            result_fact = self.fact()
            return result_term / result_fact
        else:
            return result_term

    def term(self):
        if self.lookahead.type == TokenType.Open:
            self.match(self.lookahead)  # it matches OPEN
            result_expr = self.expr()   # it gets the expression
            self.match(self.lookahead)  # it matches CLOSE
            return result_expr
        elif self.lookahead.type == TokenType.Var:
            name = self.lookahead.attribute
            self.match(self.lookahead)
            return self.lexer.symbol_table[name]
        elif self.lookahead.type == TokenType.Int:
            value = int(self.lookahead.attribute)
            self.match(self.lookahead)
            return value
        elif self.lookahead.type == TokenType.Float:
            value = float(self.lookahead.attribute)
            self.match(self.lookahead)
            return value

    def match(self, token):
        if (self.lookahead.type == token.type
                and self.lookahead.attribute == token.attribute):
            self.lookahead = self.lexer.next_token()
        else:
            print("*** Syntax Error! Values do not match. ***")