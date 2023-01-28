grammar Grammar;

program: cmd=command EOF #PGCLProgram
  ;

postexpectation: 'post:' exp=expectation EOF #PostExpectation
  ;

preexpectation: 'pre:' cons=constraint EOF #PreExpectation
  ;

inits: 'init:' init=initialization EOF #Initializations
  ;

expression: // PGCL Arithmetic Expressions                                     
  expr1=expression op=(TIMES|DIV) expr2=expression                #MultDivExpr    // Multiplication, Division
  | expr1=expression op=(PLUS|MINUS|DOTMINUS) expr2=expression    #PlusMinusDotminusExpr     // Addition, Subtraction, Non-negative Subtraction
  | num=INT                                                       #IntExpr      // Integer
  | LPAR expr=expression RPAR                                     #Expr         // Parenthesized expression 
  | var=VAR                                                       #VarExpr      // Variable
  ;

aexpectation: // Expectation Arithmetic Expressions                                        
  aexp1=aexpectation op=(TIMES|DIV) aexp2=aexpectation                #MultDivAExp    /// Multiplication, Division
  | aexp1=aexpectation op=(PLUS|MINUS|DOTMINUS) aexp2=aexpectation    #PlusMinusDotminusAExp     // Addition, Subtraction, Non-negative Subtraction
  | LPAR aexp=aexpectation RPAR                                       #ExprAExp     // Parentesized expression
  | num=INT                                                           #IntAExp      // Integer
  | num=FLOAT                                                         #RealAExp     // Real
  | var=VAR                                                           #VarAExp      // Variable 
  ;

bexpression: // PGCL Boolean Expression
  val=(TRUE | FALSE)                                              #BoolExpr     // Boolean value
  | op=NEG bexpr=bexpression                                      #NegExpr      // Negation
  | bexpr1=bexpression op=AND bexpr2=bexpression                  #AndExpr      // Conjunction
  | bexpr1=bexpression op=OR bexpr2=bexpression                   #OrExpr       // Disjunction
  | bexpr1=expression op=(EQ|NEQ|GT|LT|GEQ|LEQ) bexpr2=expression #CompareExpr  // Comparative expression
  | LPAR bexpr=bexpression RPAR                                   #BExpr        // Paranthesized expression
  ;

bexpectation: // Expectation Boolean Expression
  val=(TRUE | FALSE)                                                 #BoolAExp   // Boolean value
  | op=NEG bexp=bexpectation                                         #NegAExp    // Negation
  | bexp1=bexpectation op=AND bexp2=bexpectation                     #AndAExp    // Conjunction
  | bexp1=bexpectation op=OR bexp2=bexpectation                      #OrAExp     // Disjunction
  | bexp1=aexpectation op=(EQ|NEQ|GT|LT|GEQ|LEQ) bexp2=aexpectation  #CompareExp // Comparative expression
  | LPAR bexp=bexpectation RPAR                                      #BAExp      // Paranthesized expression
  ;

command : // PGCL command
  var=VAR ASS expr=expression                                                                   #AssCmd     // Assignment         (assign to an arithmetic expression)
  | var=VAR ASS UNIF LPAR lower=INT RANGE upper=INT RPAR                                        #UnifCmd    // Uniform assignment (assign to a uniform expression)
  | SKIIP                                                                                       #SkipCmd    // Skip               (effectless program)
  | cmd1=command SEQ cmd2=command                                                               #SeqCmd     // Sequential Composition
  | LCPAR cmd1=command RCPAR LSPAR expr=expression RSPAR LCPAR cmd2=command RCPAR               #ProbCmd    // Probabilistic Choice 
  | LCPAR cmd1=command RCPAR LSPAR RSPAR LCPAR cmd2=command RCPAR                               #NonDetCmd  // Non-deterministic Choice 
  | IF LPAR bexpr=bexpression RPAR LCPAR cmdIf=command RCPAR ELSE LCPAR cmdElse=command RCPAR   #IfElseCmd  // Conditional Choice
  | WHILE LPAR bexpr=bexpression RPAR LSPAR inv=expectation RSPAR LCPAR cmd=command RCPAR       #WhileCmd   // While loop
  ;

// Expectation
expectation: aexpectation
  | expectation0
  ;

aexppar: // Expectation Arithmetic Expressions (to keep precedence when combining arithmetic expression with guarding/addition/scaling expectation)                                   
  LPAR aexp=aexpectation RPAR                        #ExprAExpPar // Parenthesized expression
  | num=INT                                          #IntAExpPar  // Integer
  | num=FLOAT                                        #RealAExpPar // Real
  | var=VAR                                          #VarAExpPar  // Variable
  ;

expectation0: // Expectation Arithmetic Expressions (considering precedence)
  exp=expectation0 TIMES LSPAR bexp=bexpectation RSPAR     #GuardExp // Guarding
  | LSPAR bexp=bexpectation RSPAR TIMES exp=expectation0   #GuardExp // Guarding
  | exp=expectation0 TIMES aexp=aexppar                    #ScalExp  // Scaling by arithmetic expressions
  | aexp=aexppar TIMES exp=expectation0                    #ScalExp  // Scaling by arithmetic expressions
  | exp1=expectation0 PLUS exp2=expectation0               #AddExp   // Addition
  | LPAR exp=expectation0 RPAR                             #Exp      // Parenthesized expectation
  | aexp=aexppar                                           #AExp     // Arithmetic expression
  | LSPAR bexp=bexpectation RSPAR                          #BExp     // Guard (Boolean expression)
  ;

constraint: // Contraint (pre-expectation)
  op=(EQ|NEQ|GT|LT|GEQ|LEQ) exp=expectation        #Cons
  ; 

initialization:                                                  #NoInit
  | left=initialization SEQ right=initialization                 #InitSeq
  | var=VAR LSPAR start=INT RANGE end=INT RSPAR ARROW init=INT   #Init
  ;



TRUE : 'true' ;
FALSE : 'false' ;
IF : 'if' ;
ELSE : 'else' ;
WHILE : 'while' ;
LPAR : '(' ;
RPAR : ')' ;
LSPAR : '[' ;
RSPAR : ']' ;
LCPAR : '{' ;
RCPAR : '}' ;
ASS : ':=' ;
NEQ : '!=' ;
GEQ : '>=' ;
LEQ : '<=' ;
AND : '&&' ;
OR : '||' ;
DOTMINUS : '.-' ;
RANGE : '..' ;
ARROW : '->' ;
GT : '>' ;
LT : '<' ;
TIMES : '*' ;
DIV : '/' ;
PLUS : '+' ;
MINUS : '-' ;
SEQ : ';' ;
NEG : '!' ;
EQ : '=' ;
UNIF : 'unif' ;
SKIIP : 'skip' ;

COMMENT : '//' ~( '\r' | '\n' )* -> skip;
MULTILINECOMMENT : '(*' .*? '*)' -> skip;
INT : [0-9]+ ;
FLOAT  : INT '.' INT ;
WHITESPACE : (' ' | '\t' )+ -> skip ;
NEWLINE : ('\n\r' | '\n' | '\r') -> skip ;
VAR : CHAR(CHAR|INT|'_')* ;
CHAR  : 'A'..'Z' | 'a'..'z' ;