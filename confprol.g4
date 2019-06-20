grammar confprol;
program   :  statement* EOF;



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
            | ids #finalIDS
            | STRING #finalSTRING
            | functionCall #finalFunctionCall
            | BOOLEAN #finalBoolean
            | FLOAT #finalFloat;

ids locals [before]  : ID #attribute
                | ids'.'ids#intermediateIDs
                | ID'('arguments?')' #call;




functionCall :  ID'(' arguments?')';
arguments   : expr',' arguments | expr;

BOOLEAN : 'True' | 'False';
INLINE_COMMENT  : '//' ~[\r\n]*  -> skip;
COMMENT: '/*' .*? '*/'  -> skip;
function_declaration:  'funko' ID '(' parameters? ')''{' statement* '}';

parameters   : ID',' parameters | ID;


FLOAT  : NUMBER+'.'NUMBER*;
ID     : [a-zA-Z]+ ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n] -> skip;


STRING: '"' (~["\\\r\n] | [\\][\\]* .)* '"';