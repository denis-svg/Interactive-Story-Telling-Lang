grammar Expr;

program: (var)* knot+ EOF;

knot : ID '{' content* '}'; 
var: var_name '=' value;
value: int|str;
int:INT;
str:'"'(ID|INT)*'"';


content: text
	| goto
	| print
	| npc
	| choice
	| var_op
    | if
	;

var_op : '[' var_name '=' expr ']';
if : '(' '(' '?' logic_expr goto ')'')';

logic_expr: logic_expr ('&''&'|'|''|') logic_expr
           | '(' logic_expr ')'
           | bool_expr
            ;
bool_expr: bool_expr ('>'|'<'|'!''='|'=''='|'>''='|'<''=') bool_expr
           | expr
           ;

expr:   expr ('*'|'/') expr
    |   expr ('+'|'-') expr
    |   int
    |   '(' expr ')'
    |   str
    | var_name
    ;

goto : '(' knot_name ')' ;
print : '(''(' var_name ')'')';
npc: '(''!' (text)+ ')';
choice: '(' '(' pair*  ')'')';
pair:'!'(text)+ goto;
knot_name: ID;
var_name:ID|INT;
text: ID|INT;

EQ : '=' ;
LPAREN : '('; 
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
GH:'"';
EXLAM: '!';
L: '[';
R: ']';
MULT: '*';
DIVIDE: '/';
SUB: '-';
ADD: '+';

INT : [0-9]+ ;
ID: [a-zA-Z_0-9?.\\,;%<>!]+; 
WS: [ \t\n\r\f]+ -> skip ;

