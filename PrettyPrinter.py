from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from Grammar.nodes.InitNodes import *
from Grammar.nodes.PGNodes import *
from GlobalVariables import *

def prettify(e) :
    #print(e.__str__() + "\n")
    # Expectations
    if isinstance(e, AExp) :
        return prettify(e.expr)
    elif isinstance(e, BExp) :
        b = prettify(e.bexpr)
        return "[" + b + "]"
    elif isinstance(e, GuardExp) :
        return "(" + prettify(e.bexp) + " * " + prettify(e.exp) + ")"
    elif isinstance(e, AddExp) :
        return "(" + prettify(e.exp1) + " + " + prettify(e.exp2) + ")"
    elif isinstance(e, ScalExp) :
        return "(" + prettify(e.aexp) + " * " + prettify(e.exp) + ")"
    elif isinstance(e, MinExp) :
        lhs = prettify(e.exp1)
        rhs = prettify(e.exp2)
        if debug :
            return "Min(" + lhs + "," + rhs + ")"
        return "If (" + lhs + ">" + rhs + "," + rhs + "," + lhs + ")"
    elif isinstance(e, Invariant) : 
        return prettify(e.inv)
    elif isinstance(e, InvIneq):
        return "(" + prettify(e.lhs) + "<=" + prettify(e.inv) + "," + str(e.modVars) +")"
    elif isinstance(e, Exp) :
        return prettify(e.exp)
    elif isinstance(e, InvIneq) :
        return "(" + prettify(e.lhs) + " \n<=\n " + prettify(e.inv) + ")"
    # Arithmetic expressions
    elif isinstance(e, IntNum) :
        if not debug:
            return e.num.__str__()
        if varIsOfReal:
            return "realNum(" + e.num.__str__() + ")"
        else :
            return "intNum(" + e.num.__str__() + ")"
    elif isinstance(e, RealNum) :
        return "real(" + e.num.__str__() + ")"
    elif isinstance(e, ProbExpr) :
        return prettify(e.expr)
    elif isinstance(e, Variable) :
        if not debug :
            return e.var
        if varIsOfReal:
            return "realVar(" + e.var + ")"
        else :
            return "intVar(" + e.var + ")"
    elif isinstance(e, TimesExpr) :
        return "(" + prettify(e.expr1) + " * " + prettify(e.expr2) + ")"
    elif isinstance(e, DivExpr) :
        if debug :
            return "(" + prettify(e.expr1) + " / " + prettify(e.expr2) + ")"
        if isinstance(e.expr1, IntNum) and isinstance(e.expr2, IntNum) :
            return "Q(" + e.expr1.num.__str__() + "," + e.expr2.num.__str__() + ")"
        return "(" + prettify(e.expr1) + " / " + prettify(e.expr2) + ")"
    elif isinstance(e, PlusExpr) :
        return "(" + prettify(e.expr1) + " + " + prettify(e.expr2) + ")"
    elif isinstance(e, MinusExpr) :
        return "(" + prettify(e.expr1) + " - " + prettify(e.expr2) + ")"
    elif isinstance(e, DotMinusExpr) :
        lhs = prettify(e.expr1)
        rhs = prettify(e.expr2)
        if debug :
            return "(" + lhs + " - " + rhs + ")"
        return "If (" + lhs + ">" + rhs + "," + lhs + "-" + rhs + ",0)"
    # Boolean expressions 
    elif isinstance(e, Boool) :
        if (e.value) :
            return "1"
        else :
            return "0"
    elif isinstance(e, AndBexpr) :
        lhs = prettify(e.bexpr1)
        rhs = prettify(e.bexpr2)
        if debug :
            return "("+ lhs + "&&" + rhs + ")"
        return "And(" + lhs + "," + rhs + ")"
    elif isinstance(e, OrBexpr) :
        lhs = prettify(e.bexpr1)
        rhs = prettify(e.bexpr2)
        if debug :
            return "("+ lhs + "||" + rhs + ")"
        return "Or(" + lhs+ "," + rhs + ")"
    elif isinstance(e, NegBexpr) :
        guard = prettify(e.bexpr)
        if debug :
            return "!("+ guard + ")"
        return "Not(" + guard + ")"
    elif isinstance(e, EqBexpr) :
        return "(" + prettify(e.expr1) + "==" + prettify(e.expr2) + ")"
    elif isinstance(e, NEqBexpr) :
        return "(" + prettify(e.expr1) + "!=" + prettify(e.expr2) + ")"
    elif isinstance(e, GTBexpr) :
        return "(" + prettify(e.expr1) + ">" + prettify(e.expr2) + ")"
    elif isinstance(e, LTBexpr) :
        return "(" + prettify(e.expr1) + "<" + prettify(e.expr2) + ")"
    elif isinstance(e, GEqBexpr) :
        return "(" + prettify(e.expr1) + ">=" + prettify(e.expr2) + ")"
    elif isinstance(e, LEqBexpr) :
        return "(" + prettify(e.expr1) + "<=" + prettify(e.expr2) + ")"
    elif isinstance(e, Expr) :
        return prettify(e.expr)
    elif isinstance(e, SkipCmd) :
        return "skip"
    elif isinstance(e, AssCmd) :
        return e.var + ":=" + prettify(e.expr)
    elif isinstance(e, UnifCmd) :
        return e.var + ":=(" + e.lower.__str__() + ".." + e.upper.__str__() + ")" 
    elif isinstance(e, SeqCmd) :
        return prettify(e.cmd1) + "; " + prettify(e.cmd2)
    elif isinstance(e, ProbCmd) :
        return "{" + prettify(e.cmd1) + "} [" + prettify(e.probExpr) + "] {" + prettify(e.cmd2) + "}"
    elif isinstance(e, NonDetCmd) :
        return "{" + prettify(e.cmd1) + "} [] {" + prettify(e.cmd2) + "}"
    elif isinstance(e, IfElseCmd) :
        return "if(" + prettify(e.bexpr) + ") {" + prettify(e.bexpr) + "}"
    elif isinstance(e, WhileCmd) :
        return "while (" + prettify(e.bexpr) + ") [" + prettify(e.inv) + "] { " + prettify(e.cmd) + " }"
    else :
        raise Exception("prettify: not implemented for this type: ", e)
    
def prettyConstraint(g, cons) :
    if isinstance(cons, Constraint) :
        if (cons.op == "<") :
            return prettify(g) < prettify(cons.exp)
        elif (cons.op == "<=") :
            return prettify(g) <= prettify(cons.exp)
        elif (cons.op == ">") :
            return prettify(g) > prettify(cons.exp)
        elif (cons.op == ">=") :
            return prettify(g) >= prettify(cons.exp)
        elif (cons.op == "==" or cons.op == '=') :
            return prettify(g) == prettify(cons.exp)
        elif (cons.op == "!=") :
            return prettify(g) != prettify(cons.exp)
        else :
            raise Exception("prettyConstraint: Not a valid operator:", cons.op)
    else :
        raise Exception("prettyConstraint: Not a valid contraint:", cons)
   



