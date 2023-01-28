from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from ExprSubstitution import *
        
def nonNegUnif(g, var, lower, upper) :
    if lower == upper :
        return exprSubstitution(g, var, IntNum(lower))
    else :
        return AndBexpr(exprSubstitution(g, var, IntNum(lower)), nonNegUnif(g, var, lower+1, upper))

def nonNegAnalysis(pgcl, q):
    if isinstance(pgcl, SkipCmd) :
        return q
    elif isinstance(pgcl, AssCmd):
        return AndBexpr(exprSubstitution(q, pgcl.var, pgcl.expr), GEqBexpr(pgcl.expr, AExp(IntNum(0))))
    elif isinstance(pgcl, UnifCmd):
        return nonNegUnif(q, pgcl.var, pgcl.lower, pgcl.upper)
    elif isinstance(pgcl, SeqCmd):
        return nonNegAnalysis(pgcl.cmd1, nonNegAnalysis(pgcl.cmd2, q))
    elif isinstance(pgcl, ProbCmd):
        return AndBexpr(nonNegAnalysis(pgcl.cmd1, q), nonNegAnalysis(pgcl.cmd2, q))
    elif isinstance(pgcl, IfElseCmd):
        lhs = ImpBexpr(pgcl.bexpr, nonNegAnalysis(pgcl.cmdIf, q))
        rhs = ImpBexpr(NegBexpr(pgcl.bexpr), nonNegAnalysis(pgcl.cmdElse, q))
        return AndBexpr(lhs, rhs)
    elif isinstance(pgcl, NonDetCmd):
        return AndBexpr(nonNegAnalysis(pgcl.cmd1, q), nonNegAnalysis(pgcl.cmd2, q))
    elif isinstance(pgcl, WhileCmd):
        body = AndBexpr(GEqBexpr(pgcl.inv, AExp(IntNum(0))), q)
        return nonNegWhile(pgcl, body)
    else :
        print(pgcl)
        raise Exception("nonNegAnalysis: not implemented for type" + pgcl.__str__())

def nonNegWhile(pgcl, body):
    if isinstance(pgcl, WhileCmd):
        modVars = getModifiedVars(pgcl.cmd, set())
        nonNegVars = varsShouldBeNonNeg(modVars.copy())
        if len(modVars) == 0 :
            rhs = ImpBexpr(pgcl.bexpr, nonNegAnalysis(pgcl.cmd, body))
        else :
            rhs = ForAllBexpr(modVars, ImpBexpr(AndBexpr(pgcl.bexpr, nonNegVars), nonNegAnalysis(pgcl.cmd, body)))
        ifGuard = ImpBexpr(pgcl.bexpr, rhs)
        ifNotGuard = ImpBexpr(NegBexpr(pgcl.bexpr), body) 
        return AndBexpr(ifGuard, ifNotGuard)

