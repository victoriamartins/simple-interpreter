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

    def atr(self):
        ref = self.lookahead.attribute  # it gets the name
        self.match(self.lookahead)  # it matches VAR
        self.match(self.lookahead)  # it matches EQ
        result_expr = self.expr()
        self.lexer.symbol_table[ref] = result_expr

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
        if self.lookahead.attribute in self.lexer.symbol_table:
            value = self.lexer.symbol_table[self.lookahead.attribute]
            print(value)
        else:
            print(f'Symbol {self.lookahead.attribute} is not defined.')
        self.match(self.lookahead)
        self.match(self.lookahead)

    def lines(self):
        if self.lookahead.type != TokenType.Invalid:
            self.prog()

    def match(self, token):
        if (self.lookahead.type == token.type
                and self.lookahead.attribute == token.attribute):
            self.lookahead = self.lexer.next_token()
        else:
            print("*** Syntax Error! Values do not match. ***")

    def expr(self):
        result_expr = self.fact()
        op_rest, result_rest = self.rest()
        if op_rest == '+':
            return result_expr + result_rest
        elif op_rest == '-':
            return result_expr - result_rest
        else:
            return result_expr

    def fact(self):
        result_term = self.term()  # number
        if (self.lookahead.type == TokenType.Mult
                or self.lookahead.type == TokenType.Div):
            op_symbol, result_op = self.op()
            if op_symbol == '*':
                return result_term * result_op
            elif op_symbol == '/':
                return result_term / result_op
        return result_term

    def rest(self):
        if (self.lookahead.type != TokenType.Invalid and
                self.lookahead.type != TokenType.Eol and
                self.lookahead.type != TokenType.Close):
            op_symbol = self.lookahead.attribute  # it gets the symbol
            self.match(self.lookahead)  # it matches the symbol
            result_expr = self.expr()
            return op_symbol, result_expr
        return 'invalid', -1

    def term(self):
        if self.lookahead.type == TokenType.Open:
            self.match(self.lookahead)
            result_expr = self.expr()
            self.match(self.lookahead)
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

    def op(self):
        op_symbol = self.lookahead.attribute
        self.match(self.lookahead)
        result = self.fact()
        return op_symbol, result
