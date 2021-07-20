from token_config import Token, TokenType


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.next_token()
        # self.lookahead = Token() TODO: to change it when I'm coding
        self.output = str()

    def match(self, token):
        if (self.lookahead.type == token.type
                and self.lookahead.attribute == token.attribute):
            self.lookahead = self.lexer.next_token()
        else:
            print("*** Syntax Error! Values do not match. ***")

    def prog(self):
        self.stmt()
        # self.lookahead = self.lexer.next_token()
        self.match(self.lookahead)
        self.lines()

    def lines(self):
        if self.lookahead.type != TokenType.Invalid:
            self.prog()

    def atr(self):
        ref = self.lookahead.attribute  # it gets the name
        self.match(self.lookahead)  # it matches VAR but todo it has to search in symbol table
        self.match(self.lookahead)
        result_expr = self.expr()
        self.lexer.symbol_table[ref] = result_expr

    def expr(self):
        result_expr = self.fact()
        op_rest, result_rest = self.rest()
        if op_rest != 'invalid':
            if op_rest == '+':
                result_expr = result_expr + result_rest
            else:
                result_expr = result_expr - result_rest
        return result_expr

    def fact(self):
        result_term = self.term()
        op_symbol = False
        if (self.lookahead.type == TokenType.Mult
                or self.lookahead.type == TokenType.Div):
            op_symbol, result_op = self.op()

        if op_symbol:
            if op_symbol == '*':
                return result_term * result_op
            elif op_symbol == '/':
                return result_term / result_op

    def rest(self):  # TODO to improve this function interpreting results
        if self.lookahead.type != TokenType.Invalid:
            op_symbol = self.lookahead.attribute  # it gets the symbol
            self.match(self.lookahead)
            result_expr = self.expr()  # todo to make it return something
            return op_symbol, result_expr
        return 'invalid', -1

    def stmt(self):
        if self.lookahead.type == TokenType.Var:
            self.atr()
        elif self.lookahead.type == TokenType.Print:
            self.imp()
        else:
            print('Syntax error: Var or print were expected.')

    def term(self):
        if self.lookahead.type == TokenType.Num:
            value = self.lookahead.attribute
            self.match(self.lookahead)
            return value
        elif self.lookahead.type == TokenType.Var:
            # content = its value in symbol_table
            try:
                content = self.lexer.symbol_table[self.lookahead.attribute]
                self.match(self.lookahead)
                return content
            except NameError:
                print(f'To write a message: {NameError}')
        elif self.lookahead.type == TokenType.Open:
            self.match(self.lookahead)  # it will match OPEN
            result_expr = self.expr()
            self.match(self.lookahead)  # I HOPE it will match CLOSE
            return result_expr

    def op(self):
        op_symbol = self.lookahead.attribute
        self.match(self.lookahead)
        result = self.fact()  # todo to make it return something
        return op_symbol, result

    def imp(self):
        for i in range(4):
            # self.lookahead = self.lexer.next_token()
            self.match(self.lookahead)  # it matches PRINT, OPEN, VAR and CLOSE
