grammar confprol;
program   :  statement* EOF;



statement : (assign |in_operations| print_  | expr | return_value | attribute_assign|import_|)';' | ( condition | function_declaration |while_not_loop) ;

import_: 'import' STRING 'as' ID;

while_not_loop: 'while' 'not' expr '{' statement* '}';

assign    : ID '==' expr ;
attribute_assign    :  expr '.' (subattributes '.')? ID '==' expr;
print_     : 'print' expr ;
condition : 'if' 'not' expr '{' statement* '}' elsecondition?;
elsecondition: 'else' '{' statement* '}';
return_value: 'run' 'away' 'with' expr;


in_operations: (ID|attributes) '=+=' expr #inOperationsSum |  (ID|attributes) '=-=' expr #inOperationsMinus|
                (ID|attributes) '=*=' expr #inOperationsMult | (ID|attributes) '=/=' expr #inOperationsDivision ;

expr      : '!' expr #negatedExpr| expr ':=' expr #exprEqual  | expr2 #exprNE ;


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
            | boolean #finalBoolean
            | FLOAT #finalFloat
            | list_creation #finalListCreation
            | '-' NUMBER #finalNegativeNumber;


attributes : (ID | STRING)'.' subattributes #attributeBeginning;
subattributes  locals[before]:    ID #attribute
                | subattributes'.'subattributes#intermediateIDs
                | ID'('arguments?')' #methodCall;



list_creation   : '[' arguments? ']';

functionCall :  ID'(' arguments?')';
arguments   : expr',' arguments | expr;

boolean : 'True' #booleanTrue | 'False' #booleanFalse | 'xTrue' #booleanXTrue
| 'xFalse' #booleanXFalse | 'yTrue' #booleanYTrue | 'yFalse' #booleanYFalse | 'TrueExceptFridays' #booleanTrueFridays
| 'MillionToOneChance' #booleanMillionToOne;
//INLINE_COMMENT  : '//' ~[\r\n]*  -> skip;
//COMMENT: '/*' .*? '*/'  -> skip;
COMMENT: '@useless_comment' [ ]* '(' .*? ')' ->skip;
OTHER_COMMENT: '@useless_comment' [ ]* '/*' .*? '*/' ->skip;
function_declaration:  'funko' ID '(' parameters? ')''{' statement* '}';

parameters   : ID',' parameters | ID;


FLOAT  : NUMBER+'.'NUMBER*;
NONE: 'None';
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n] -> skip;
NUMBERED_ID  : [a-zA-Z0-9]+;

STRING: '"' (~["\\\r\n] | [\\] .)* '"';
OTHERCHARACTER : . ; /* To avoid token recognition errors with characters like "`" */