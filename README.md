# simple-interpreter

This is a simple interpreter which uses the following grammar:

```
<prog>  ::= <stmt> <EOL> <lines>
<lines> ::= <prog> | ε
<imp>   ::= <PRINT> <OPEN> <VAR> <CLOSE>
<atr>   ::= <VAR> <EQ> <expr>
<op>    ::= <MULT> <fact> | <DIV> <fact>
<expr>  ::= <fact> <rest>
<rest>  ::= <SUM> <expr> | <SUB> <expr> | vazio
<fact>  ::= <term> <op> | <term>
<term>  ::= <OPEN> <expr> <CLOSE> | <NUM> | <VAR>
<stmt>  ::= <atr> | <imp>
<EOL>   ::= ;
<PRINT> ::= print
<OPEN>  ::= (
<VAR>   ::= $ followed by a set of alphanumeric symbols
<CLOSE> ::= )
<EQ>    ::= =
<MULT>  ::= *
<DIV>   ::= /
<SUM>   ::= +
<SUB>   ::= -
<NUM>   ::= 0 | 1 | ... | 8 | 9
```