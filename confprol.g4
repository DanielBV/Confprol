grammar confprol;
program   :  statement* EOF;



statement : (assign | print_  | expr | return_value | attribute_assign|import_)';' | ( condition | function_declaration) ;

import_: 'import' STRING 'as' ID;



assign    : ID '=' expr ;
attribute_assign    :  expr '.' (subattributes '.')? ID '=' expr;
print_     : 'print' expr ;
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
            | NONE #finalNone
            | ID #finalID
            | attributes #finalIDS
            | STRING #finalSTRING
            | functionCall #finalFunctionCall
            | BOOLEAN #finalBoolean
            | FLOAT #finalFloat
            | list_creation #finalListCreation
            | '-' NUMBER #finalNegativeNumber;


attributes locals [before]: (ID | STRING)'.' subattributes #attributeBeginning;
subattributes  locals[before]:    ID #attribute
                | subattributes'.'subattributes#intermediateIDs
                | ID'('arguments?')' #methodCall;



list_creation   : '[' arguments? ']';

functionCall :  ID'(' arguments?')';
arguments   : expr',' arguments | expr;

BOOLEAN : 'True' | 'False';
INLINE_COMMENT  : '//' ~[\r\n]*  -> skip;
COMMENT: '/*' .*? '*/'  -> skip;
function_declaration:  'funko' ID '(' parameters? ')''{' statement* '}';

parameters   : ID',' parameters | ID;


FLOAT  : NUMBER+'.'NUMBER*;
NONE: 'None';
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n] -> skip;
NUMBERED_ID  : [a-zA-Z0-9]+;

STRING: '"' (~["\\\r\n] | [\\][\\]* .)* '"';
OTHERCHARACTER : . ; /* To avoid token recognition errors with characters like "`" */