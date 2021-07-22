from token_config import Token, TokenType


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.next_token()
        # self.lookahead = Token() TODO: to change it when I'm coding
        self.output = str()

    # ok
    def atr(self):
        ref = self.lookahead.attribute  # it gets the name
        self.match(self.lookahead)  # it matches VAR
        self.match(self.lookahead)  # it matches EQ
        result_expr = self.expr()
        self.lexer.symbol_table[ref] = result_expr

    # ok
    def stmt(self):
        if self.lookahead.type == TokenType.Var:
            self.atr()
        elif self.lookahead.type == TokenType.Print:
            self.imp()
        else:
            print('Syntax error: Var or print were expected.')

    # ok
    def imp(self):
        self.match(self.lookahead)  # print
        self.match(self.lookahead)  # open
        value = self.lexer.symbol_table[self.lookahead.attribute]
        self.match(self.lookahead)  # var
        self.match(self.lookahead)  # close
        print(value)

    # ok
    def lines(self):
        if self.lookahead.type != TokenType.Invalid:
            self.prog()

    def match(self, token):
        if (self.lookahead.type == token.type
                and self.lookahead.attribute == token.attribute):
            self.lookahead = self.lexer.next_token()
        else:
            print("*** Syntax Error! Values do not match. ***")

    def prog(self):
        self.stmt()
        self.match(self.lookahead)
        self.lines()

    def expr(self):
        result_expr = self.fact()  # number
        op_rest, result_rest = self.rest()  # returns sum sub or nothing
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
        if self.lookahead.type != TokenType.Invalid:
            op_symbol = self.lookahead.attribute  # it gets the symbol
            self.match(self.lookahead)  # it maches the symbol
            result_expr = self.expr()  # todo to make it return something
            return op_symbol, result_expr
        return 'invalid', -1

    def term(self):
        if self.lookahead.type == TokenType.Open:
            return self.expr()
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
        result = self.fact()  # todo to make it return something
        return op_symbol, result
