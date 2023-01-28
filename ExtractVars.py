from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *


def extractVariables(pgcl, vars=set) -> set :
    # Commands
    if isinstance(pgcl, SkipCmd) :
        return vars
    elif isinstance(pgcl, AssCmd) :
        expr = extractVariables(pgcl.expr,vars)
        vars.add(pgcl.var)
        return vars.union(expr)
    elif isinstance(pgcl, UnifCmd) :
        vars.add(pgcl.var)
        return vars
    elif isinstance(pgcl, SeqCmd) :
        lhs = extractVariables(pgcl.cmd1, vars)
        rhs = extractVariables(pgcl.cmd2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, ProbCmd) :
        lhs = extractVariables(pgcl.cmd1, vars)
        prob = extractVariables(pgcl.probExpr, vars)
        rhs = extractVariables(pgcl.cmd2, vars)
        return lhs.union(rhs, prob)
    elif isinstance(pgcl, NonDetCmd) :
        lhs = extractVariables(pgcl.cmd1, vars)
        rhs = extractVariables(pgcl.cmd2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, IfElseCmd) :
        guard = extractVariables(pgcl.bexpr, vars)
        ifCmd = extractVariables(pgcl.cmdIf, vars)
        elseCmd = extractVariables(pgcl.cmdElse, vars)
        return guard.union(ifCmd, elseCmd)
    elif isinstance(pgcl, WhileCmd) : 
        guard = extractVariables(pgcl.bexpr, vars)
        inv = extractVariables(pgcl.inv, vars)
        body = extractVariables(pgcl.cmd, vars)
        return guard.union(inv, body)
    elif isinstance(pgcl, Invariant) :
        return extractVariables(pgcl.inv, vars)
    # Expectations
    elif isinstance(pgcl, AExp) :
        return extractVariables(pgcl.expr, vars)
    elif isinstance(pgcl, BExp) :
        return extractVariables(pgcl.bexpr, vars)
    elif isinstance(pgcl, Exp) :
        return extractVariables(pgcl.exp, vars)
    elif isinstance(pgcl, GuardExp) :
        bexp = extractVariables(pgcl.bexp, vars)
        exp = extractVariables(pgcl.exp, vars)
        return bexp.union(exp)
    elif isinstance(pgcl, AddExp) :
        lhs = extractVariables(pgcl.exp1, vars)
        rhs = extractVariables(pgcl.exp2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, ScalExp) :
        aexp = extractVariables(pgcl.aexp, vars)
        exp = extractVariables(pgcl.exp, vars)
        return aexp.union(exp)
    # BExpressions
    elif isinstance(pgcl, Boool) :
        return vars
    elif isinstance(pgcl, AndBexpr) :
        lhs = extractVariables(pgcl.bexpr1, vars)
        rhs = extractVariables(pgcl.bexpr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl,OrBexpr) : 
        lhs = extractVariables(pgcl.bexpr1, vars)
        rhs = extractVariables(pgcl.bexpr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, NegBexpr) :
        return extractVariables(pgcl.bexpr, vars)
    elif isinstance(pgcl, EqBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, NEqBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, GTBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, LTBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        lhs.union(rhs)
        return lhs
    elif isinstance(pgcl, GEqBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, LEqBexpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, BExpr) :
        return extractVariables(pgcl.bexpr, vars)
    #AExpressions
    elif isinstance(pgcl, Variable) :
        vars.add(pgcl.var)
        return vars
    elif isinstance(pgcl, IntNum) :
        return vars
    elif isinstance(pgcl, RealNum) :
        return vars
    elif isinstance(pgcl, TimesExpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, DivExpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, PlusExpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, MinusExpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, DotMinusExpr) :
        lhs = extractVariables(pgcl.expr1, vars)
        rhs = extractVariables(pgcl.expr2, vars)
        return lhs.union(rhs)
    elif isinstance(pgcl, Expr) :
        return extractVariables(pgcl.expr, vars)
    elif isinstance(pgcl, ProbExpr) :
        return extractVariables(pgcl.expr, vars)
    else :
        raise Exception("extractVariables: not implemented for " + pgcl.__str__())