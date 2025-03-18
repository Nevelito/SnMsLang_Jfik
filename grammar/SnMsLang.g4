grammar SnMsLang;

program: statement+ ;

statement: assignment
         | printStmt
         | readStmt
         | ifStmt
         | whileStmt
         | funcDecl
         | generatorDecl
         | varDecl
         | classDecl
         | structDecl
         | returnStmt
         | yieldStmt
         ;

assignment: ID '=' expr ';' ;

printStmt: 'wypisz' '(' expr ')' ';' ;

readStmt: 'wczytaj' '(' ID ')' ';' ;

ifStmt: 'jezeli' '(' expr ')' block ('inaczej' block)? ;

whileStmt: 'dopoki' '(' expr ')' block ;

returnStmt: 'zwroc' expr ';' ;

yieldStmt: 'yield' expr ';' ;

block: '{' statement* '}' ;

funcDecl: 'funkcja' ID '(' paramList? ')' block ;

generatorDecl: 'generator' ID '(' paramList? ')' block ;

classDecl: 'klasa' ID '{' (varDecl | funcDecl)* '}' ;

structDecl: 'struktura' ID '{' varDecl* '}' ;

varDecl: ('globalna' | 'lokalna')? typ ID ('[' INT (',' INT)* ']')* ';' ;

paramList: param (',' param)* ;
param: typ? ID ;

expr: expr ('*' | '/') expr    # MulDivExpr
    | expr ('+' | '-') expr    # AddSubExpr
    | expr ('==' | '!=' | '<' | '>' | '<>') expr  # CompareExpr
    | expr ('&&' | '||' | '^') expr  # LogicalExpr
    | ID '[' expr (',' expr)* ']'    # ArrayExpr
    | ID                             # IdExpr
    | INT                            # IntExpr
    | FLOAT                          # FloatExpr
    | STRING                         # StringExpr
    | BOOL                           # BoolExpr
    | '(' expr ')'                   # ParenExpr
    | '!' expr                       # NotExpr
    ;

typ: 'liczba'
    | 'zmiennoprzecinkowa' ('32' | '64')?
    | 'tekst'
    | 'bool'
    | 'zmienna'
    | 'dynamiczny'
    ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
INT: [0-9]+ ;
FLOAT: [0-9]+ '.' [0-9]+ ;
STRING: '"' (~["\r\n])* '"' ;
BOOL: 'prawda' | 'falsz' ;

WS: [ \t\r\n]+ -> skip ;

ERROR_CHAR: . {System.err.println("Nieoczekiwany znak: " + getText());} -> skip ;
