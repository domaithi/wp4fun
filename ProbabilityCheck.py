from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from ExprSubstitution import *


def probAnalysisUnif(q, var, lower, upper) :
    if lower == upper :
        return exprSubstitution(q, var, IntNum(lower))
    else :
        return AndBexpr(exprSubstitution(q, var, IntNum(lower)), probAnalysisUnif(q, var, lower+1, upper))

def probAnalysis(pgcl, q) :
    if isinstance(pgcl, SkipCmd) :
        return q
    elif isinstance(pgcl, AssCmd):
        return exprSubstitution(q, pgcl.var, pgcl.expr)
    elif isinstance(pgcl, UnifCmd):
        return probAnalysisUnif(q, pgcl.var, pgcl.lower, pgcl.upper)
    elif isinstance(pgcl, ProbCmd): 
        lhs = probAnalysis(pgcl.cmd1, q)
        rhs = probAnalysis(pgcl.cmd2, q)
        leq = AndBexpr(LEqBexpr(IntNum(0), pgcl.probExpr), LEqBexpr(pgcl.probExpr, IntNum(1)))
        return AndBexpr(leq, AndBexpr(lhs, rhs))
    elif isinstance(pgcl, SeqCmd):
        return probAnalysis(pgcl.cmd1, probAnalysis(pgcl.cmd2, q))
    elif isinstance(pgcl, IfElseCmd):
        lhs = probAnalysis(pgcl.cmdIf, q)
        rhs = probAnalysis(pgcl.cmdElse, q)
        return AndBexpr(lhs, rhs)
    elif isinstance(pgcl, NonDetCmd):
        return AndBexpr(probAnalysis(pgcl.cmd1, q), probAnalysis(pgcl.cmd2, q))
    elif isinstance(pgcl, WhileCmd):
        return probWhile(pgcl, q)
    else :
        raise Exception("probAnalysis: not implemented for type " + pgcl)
    
def probWhile(pgcl, q) :
    if isinstance(pgcl, WhileCmd) :
        modVars = getModifiedVars(pgcl.cmd, set())
        nonNegVars = varsShouldBeNonNeg(modVars.copy())
        if len(modVars) == 0 : 
            # If no vars are modified, the solvers won't allow forall
            rhs = ImpBexpr(pgcl.bexpr, probAnalysis(pgcl.cmd, q))
        else :
            rhs = ForAllBexpr(modVars, ImpBexpr(AndBexpr(pgcl.bexpr, nonNegVars), probAnalysis(pgcl.cmd, q)))
        ifGuard = ImpBexpr(pgcl.bexpr, rhs)
        ifNotGuard = ImpBexpr(NegBexpr(pgcl.bexpr), q) 
        return AndBexpr(ifGuard, ifNotGuard)
