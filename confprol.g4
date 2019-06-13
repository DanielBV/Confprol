grammar confprol;
program   :  statement*;



statement : (assign | print  | expr | return_value)';' | ( condition | function_declaration) ;

assign    : ID '=' expr ;
print     : 'print' expr ;
condition : 'if' expr '{' statement* '}' elsecondition?;
elsecondition: 'else' '{' statement* '}';
return_value: 'return' expr;

expr      : expr2 '==' expr2 #exprEqual | expr2 #exprNE;


expr2: expr2 '+' term #exprSUM
        | expr2 '-' term #exprMINUS
        | term #exprTERM ;

term      : term '*' final #termMULT
            |term '/' final  #termDIV
            | final #termFINAL;
final     : '('expr')' #finalPAR
            | NUMBER #finalNUMBER
            | ID #finalID
            | STRING #finalSTRING
            | methodCall #finalMethodCall;

methodCall :  ID'(' arguments?')';
arguments   : expr',' arguments | expr;


function_declaration:  'funko' ID '(' parameters? ')''{' statement* '}';

parameters   : ID',' parameters | ID;

ID     : [a-zA-Z]+ ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n] -> skip;

STRING: '"' (~["\\\r\n] | [\\][\\]* .)* '"';