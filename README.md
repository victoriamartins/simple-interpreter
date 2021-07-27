# simple-interpreter

This is a simple interpreter which uses the following grammar:

```
<prog>  ::= <stmt> <EOL> <lines>
<lines> ::= <prog> | ε
<stmt>  ::= <atr> | <imp>
<imp>   ::= <PRINT> <OPEN> <VAR> <CLOSE>
<atr>   ::= <VAR> <EQ> <expr>
<expr>  ::= fact SUM expr 
            | fact SUB expr 
            | fact 
<fact>  ::= <term> <MULT> <fact> 
            | <term> <DIV> <fact> 
            | <term>
<term>  ::= <OPEN> <expr> <CLOSE> 
            | <NUM> 
            | <VAR>
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