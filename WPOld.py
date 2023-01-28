from Z3Solver import *
from CVC5Solver import *
import time
from ExprSubstitution import *

################################
# Credits: 
# The Weakest Preexpectation (wp) analysis is based on the work of 
# Benjamin Lucien Kaminski,
# Advanced weakest precondition calculi for probabilistic programs,
# http://publications.rwth-aachen.de/record/755408/files/755408.pdf
###############################

def wpSubstitutionOld(g, x, e) :
    # Expectations
    if isinstance(g, AExp) :
        return wpSubstitutionOld(g.expr, x, e)
    elif isinstance(g, BExp) :
        return wpSubstitutionOld(g.bexpr, x, e)
    elif isinstance(g, GuardExp) :
        return GuardExp(wpSubstitutionOld(g.bexp, x, e), wpSubstitutionOld(g.exp, x, e))
    elif isinstance(g, AddExp) :
        return AddExp(wpSubstitutionOld(g.exp1, x, e), wpSubstitutionOld(g.exp2, x, e))
    elif isinstance(g, ScalExp) :
        return ScalExp(wpSubstitutionOld(g.aexp, x, e), wpSubstitutionOld(g.exp, x, e))
    elif isinstance(g, MinExp) :
        return MinExp(wpSubstitutionOld(g.exp2, x, e), wpSubstitutionOld(g.exp1, x, e))
    elif isinstance(g, Invariant):
        return wpSubstitutionOld(g.inv, x, e)
    elif isinstance(g, Exp) :
        return wpSubstitutionOld(g.exp, x, e)
    # AExpressions
    elif isinstance(g, IntNum) :
        return AExp(g)
    elif isinstance(g, RealNum) :
        return AExp(g)
    elif isinstance(g, ProbExpr) :
        return AExp(ProbExpr(wpSubstitutionOld(g.expr, x, e)))
    elif isinstance(g, Variable) :
        if g.var == x :
            return AExp(e)
        else :
            return AExp(g)
    elif isinstance(g, TimesExpr) :
        return AExp(TimesExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, DivExpr) :
        return AExp(DivExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, PlusExpr) :
        return AExp(PlusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, MinusExpr) :
        return AExp(MinusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, DotMinusExpr) :
        return AExp(DotMinusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, Expr):
        return wpSubstitutionOld(g.expr, x, e)
    # BExpressions
    elif isinstance(g, Boool) :
        return BExp(g)
    elif isinstance(g, NegBexpr) :
        return BExp(NegBexpr(exprSubstitution(g.bexpr, x, e)))
    elif isinstance(g, AndBexpr) :
        return BExp(AndBexpr(exprSubstitution(g.bexpr1, x, e), exprSubstitution(g.bexpr2, x, e)))
    elif isinstance(g, OrBexpr) :
        return BExp(OrBexpr(exprSubstitution(g.bexpr1, x, e), exprSubstitution(g.bexpr2, x, e)))
    elif isinstance(g, EqBexpr) :
        return BExp(EqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, NEqBexpr) :
        return BExp(NEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, GEqBexpr) :
        return BExp(GEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, GTBexpr) :
        return BExp(GTBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, LEqBexpr) :
        return BExp(LEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, LTBexpr) :
        return BExp(LTBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    elif isinstance(g, ImpBexpr):
        return BExp(ImpBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e)))
    # Used for old WP
    elif isinstance(g, int) :
        return AExp(IntNum(g))
    elif isinstance(g, float) :
        return AExp(RealNum(g))
    else :
        print("\nG = ", g, '\n')
        raise Exception("wpSubstitutionOld: Not implemented for type " + str(type(g)))


def unifSummationOld(g, var, lower, upper) :
    if lower == upper :
        return wpSubstitutionOld(g, var, IntNum(lower))
    else :

        return AddExp(wpSubstitutionOld(g, var, IntNum(lower)), unifSummationOld(g, var, lower+1, upper))


def wp_old(pgcl, g, solver, vars, runTime):
    if isinstance(pgcl, SkipCmd) :
        return g, runTime
    elif isinstance(pgcl, AssCmd):
        return wpSubstitutionOld(g, pgcl.var, pgcl.expr), runTime
    elif isinstance(pgcl, UnifCmd):
        p = DivExpr(pgcl.lower, IntNum(pgcl.upper-pgcl.lower+1)) #Prob(1, pgcl.upper)
        return ScalExp(p, unifSummationOld(g, pgcl.var, pgcl.lower, pgcl.upper)), runTime
    elif isinstance(pgcl, SeqCmd):
        g1, rt1 = wp_old(pgcl.cmd2, g, solver, vars, runTime)
        return wp_old(pgcl.cmd1, g1, solver, vars, rt1)
    elif isinstance(pgcl, ProbCmd):
        lhs, rt1 = wp_old(pgcl.cmd1, g, solver, vars, 0.0)
        rhs, rt2 = wp_old(pgcl.cmd2, g, solver, vars, 0.0)
        return AddExp(ScalExp(pgcl.probExpr, lhs), ScalExp(MinusExpr(IntNum(1), pgcl.probExpr), rhs)), runTime+rt1+rt2 
    elif isinstance(pgcl, IfElseCmd):
        lhs, rt1 = wp_old(pgcl.cmdIf, g, solver, vars, 0.0)
        rhs, rt2 = wp_old(pgcl.cmdElse, g, solver, vars, 0.0)
        return AddExp(GuardExp(pgcl.bexpr, lhs), GuardExp(NegBexpr(pgcl.bexpr), rt2)), runTime+rt1+rt2
    elif isinstance(pgcl, NonDetCmd):
        lhs, rt1 = wp_old(pgcl.cmd1, g, solver, vars, 0.0)
        rhs, rt2 = wp_old(pgcl.cmd2, g, solver, vars, 0.0)
        return MinExp(lhs, rhs), runTime+rt1+rt2
    elif isinstance(pgcl, WhileCmd):
        lhs, rt1 = wp_old(pgcl.cmd, pgcl.inv, solver, vars, 0.0)
        invCheck = AddExp(GuardExp(NegBexpr(pgcl.bexpr), g), GuardExp(pgcl.bexpr,lhs)) 
        constraint = Constraint("<=", pgcl.inv)

        startTime = time.time()
        if solver.lower() == "z3" :
            isValidInvariant = invCheckZ3(LEqBexpr(invCheck, pgcl.inv), vars)
            #isValidInvariant = solveZ3(invCheck, constraint, vars)
        elif solver.lower() == "cvc5" :
            isValidInvariant = solveCVC5(invCheck, constraint, vars)
        else :
            raise Exception("wp_old not implemented for solver: ", solver) 
        
        rt2 = (time.time()-startTime)

        if isValidInvariant:
            return pgcl.inv, runTime+rt1+rt2
        else:
            raise Exception(solver + ": The invariant did not pass the check: " + pgcl.inv.__str__())        
    else :
        print(pgcl)
        raise Exception("wp_old: not implemented for type " + pgcl)