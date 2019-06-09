grammar confprol;
program   : 'begin' statement+ 'end';
          
statement : assign | print | condition;

assign    : ID '=' expr ;
print     : 'print' expr ;
condition : 'if' expr '{' statement* '}' elsecondition?;
elsecondition: 'else' '{' statement* '}';


expr      : expr '+' term #exprSUM
            | expr '-' term #exprMINUS
            | term #exprTERM ;
term      : term '*' final #termMULT
            |term '/' final  #termDIV
            | final #termFINAL;
final     : '('expr')' #finalPAR
            | NUMBER #finalNUMBER
            | ID #finalID
            | STRING #finalSTRING;




ID     : [a-z]+ ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n] -> skip;

STRING: '"' (~["\\\r\n] | [\\][\\]* .)* '"';