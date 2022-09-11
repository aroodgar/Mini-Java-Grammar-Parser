grammar MiniJavaASTGrammar;

// Parser
program returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : mainClass classDeclaration* EOF
    ;

mainClass returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : CLASS identifier LBRACE PUBLIC STATIC VOID 'main'
      LPAREN 'String' LBRACK RBRACK identifier RPAREN LBRACE statement RBRACE RBRACE
    ;

classDeclaration returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : CLASS identifier (EXTENDS identifier)? LBRACE varDeclaration* methodDeclaration* RBRACE
    ;

methodDeclaration returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : PUBLIC type identifier LPAREN (type identifier (COMMA type identifier)* )? RPAREN
      LBRACE varDeclaration* statement* RETURN expression SEMI RBRACE
    ;

varDeclaration returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : type identifier SEMI
    ;

type returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : INT LBRACK RBRACK #type0
    | BOOLEAN #type1
    | INT #type2
    ;

statement returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : LBRACE statement* RBRACE #statement0
    | IF LPAREN expression RPAREN statement ELSE statement #statement1
    | WHILE LPAREN expression RPAREN statement #statement2
    | 'System.out.println' LPAREN expression RPAREN SEMI #statement3
    | identifier ASSIGN expression SEMI #statement4
    | identifier LBRACK expression RBRACK ASSIGN expression SEMI #statement5
    ;

expression returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : expression (AND | LT | ADD | SUB | MUL) expression #expression0
    | expression LBRACK expression RBRACK #expression1
    | expression DOT 'length' #expression2
    | expression DOT identifier LPAREN (expression (COMMA expression)* )? RPAREN #expression3
    | INTEGER_LITERAL #expression4
    | 'true' #expression5
    | 'false' #expression6
    | identifier #expression7
    | THIS #expression8
    | NEW INT LBRACK expression RBRACK #expression9
    | NEW identifier LPAREN RPAREN #expression10
    | BANG expression #expression11
    | LPAREN expression RPAREN #expression12
    ;

identifier returns [value_attr = str(), type_attr = str(), name_attr = str()]
    : IDENTIFIER
    ;

// Lexer

// Keywords
INT:                'int';
NEW:                'new';
ELSE:               'else';
IF:                 'if';
WHILE:              'while';
BOOLEAN:            'boolean';
PUBLIC:             'public';
THIS:               'this';
RETURN:             'return';
EXTENDS:            'extends';
VOID:               'void';
CLASS:              'class';
STATIC:             'static';

// Separators
LPAREN:             '(';
RPAREN:             ')';
LBRACE:             '{';
RBRACE:             '}';
LBRACK:             '[';
RBRACK:             ']';
SEMI:               ';';
COMMA:              ',';
DOT:                '.';

// Operators
ASSIGN:             '=';
AND:                '&&';
LT:                 '<';
BANG:               '!';
ADD:                '+';
SUB:                '-';
MUL:                '*';

// Whitespace and comments
WS:                 [ \t\r\n\u000C]+ -> channel(HIDDEN);
COMMENT:            '/*' .*? '*/'    -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]*    -> channel(HIDDEN);

// Identifiers
IDENTIFIER:         Letter LetterOrDigit*;

// Literalls
INTEGER_LITERAL:    ('0' | [1-9] (Digits? | '_'+ Digits)) [lL]?;

// Fragments
fragment Digits
    : [0-9] ([0-9_]* [0-9])?
    ;

fragment LetterOrDigit
    : Letter
    | [0-9]
    ;

fragment Letter
    : [a-zA-Z$_] // these are the "java letters" below 0x7F
    | ~[\u0000-\u007F\uD800-\uDBFF] // covers all characters above 0x7F which are not a surrogate
    | [\uD800-\uDBFF] [\uDC00-\uDFFF] // covers UTF-16 surrogate pairs encodings for U+10000 to U+10FFFF
    ;
