from Z3Solver import *
from CVC5Solver import *
import time
from ExprSubstitution import *
from ExtractVars import *
from PRISMConverter import *

################################
# Credits: 
# The Weakest Preexpectation (wp) analysis is based on the work of 
# Benjamin Lucien Kaminski,
# Advanced weakest precondition calculi for probabilistic programs,
# http://publications.rwth-aachen.de/record/755408/files/755408.pdf
###############################

def wpSubstitution(g, x, e, modVars) :
    # Expectations
    if isinstance(g, AExp) :
        return wpSubstitution(g.expr, x, e, modVars)
    elif isinstance(g, BExp) :
        if isinstance(g.bexpr, InvIneq) :
            return BExp(wpSubstitution(g.bexpr, x, e, modVars))
        return wpSubstitution(g.bexpr, x, e, modVars)
    elif isinstance(g, GuardExp) :
        return GuardExp(wpSubstitution(g.bexp, x, e, modVars), wpSubstitution(g.exp, x, e, modVars))
    elif isinstance(g, AddExp) :
        return AddExp(wpSubstitution(g.exp1, x, e, modVars), wpSubstitution(g.exp2, x, e, modVars))
    elif isinstance(g, ScalExp) :
        return ScalExp(wpSubstitution(g.aexp, x, e, modVars), wpSubstitution(g.exp, x, e, modVars))
    elif isinstance(g, MinExp) :
        return MinExp(wpSubstitution(g.exp2, x, e, modVars), wpSubstitution(g.exp1, x, e, modVars))
    elif isinstance(g, Invariant):
        return wpSubstitution(g.inv, x, e, modVars)
    elif isinstance(g, Exp) :
        return wpSubstitution(g.exp, x, e, modVars)
    elif isinstance(g, InvIneq) :
        mv = modVars.union(g.modVars)
        return InvIneq(wpSubstitution(g.lhs, x, e, mv.copy()), wpSubstitution(g.inv, x, e, mv.copy()), mv.copy())
    elif isinstance(g, InvGuard) :
        return InvGuard(wpSubstitution(g.invIneq, x, e, modVars),  wpSubstitution(g.inv, x, e, modVars))
    # AExpressions
    elif isinstance(g, IntNum) :
        return AExp(g)
    elif isinstance(g, RealNum) :
        return AExp(g)
    elif isinstance(g, ProbExpr) :
        return AExp(ProbExpr(wpSubstitution(g.expr, x, e, modVars)))
    elif isinstance(g, Variable) :
        expVars = extractVariables(e, set())    
        if (g.var == x) and (g.var not in modVars) and (not expVars.intersection(modVars)):
            return AExp(e)
        else :
            return AExp(g)
    elif isinstance(g, TimesExpr) :
        return AExp(TimesExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, DivExpr) :
        return AExp(DivExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, PlusExpr) :
        return AExp(PlusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, MinusExpr) :
        return AExp(MinusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, DotMinusExpr) :
        return AExp(DotMinusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, Expr):
        return wpSubstitution(g.expr, x, e, modVars)
    # BExpressions
    elif isinstance(g, Boool) :
        return BExp(g)
    elif isinstance(g, NegBexpr) :
        return BExp(NegBexpr(exprSubstitutionWithModVars(g.bexpr, x, e, modVars)))
    elif isinstance(g, AndBexpr) :
        return BExp(AndBexpr(exprSubstitutionWithModVars(g.bexpr1, x, e, modVars), exprSubstitutionWithModVars(g.bexpr2, x, e, modVars)))
    elif isinstance(g, OrBexpr) :
        return BExp(OrBexpr(exprSubstitutionWithModVars(g.bexpr1, x, e, modVars), exprSubstitutionWithModVars(g.bexpr2, x, e, modVars)))
    elif isinstance(g, EqBexpr) :
        return BExp(EqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, NEqBexpr) :
        return BExp(NEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, GEqBexpr) :
        return BExp(GEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, GTBexpr) :
        return BExp(GTBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, LEqBexpr) :
        return BExp(LEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, LTBexpr) :
        return BExp(LTBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    elif isinstance(g, ImpBexpr):
        return BExp(ImpBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars)))
    # Used for old WP
    elif isinstance(g, int) :
        return AExp(IntNum(g))
    elif isinstance(g, float) :
        return AExp(RealNum(g))
    else :
        print("\nG = ", g, '\n')
        raise Exception("wpSubstitution: Not implemented for type " + str(type(g)))

def unifSummation(g, var, lower, upper, modVars) :
    if lower == upper :
        return wpSubstitution(g, var, IntNum(lower), modVars)
    else :
        return AddExp(wpSubstitution(g, var, IntNum(lower), modVars), unifSummation(g, var, lower+1, upper, modVars))

def wp(pgcl, g):
    if isinstance(pgcl, SkipCmd) :
        return g
    elif isinstance(pgcl, AssCmd):
        return wpSubstitution(g, pgcl.var, pgcl.expr, set())
    elif isinstance(pgcl, UnifCmd):
        p = DivExpr(IntNum(1), IntNum(pgcl.upper-pgcl.lower+1)) 
        wpUnifSum = unifSummation(g, pgcl.var, pgcl.lower, pgcl.upper, set())
        return ScalExp(p, wpUnifSum)
    elif isinstance(pgcl, SeqCmd):
        return wp(pgcl.cmd1, wp(pgcl.cmd2, g))
    elif isinstance(pgcl, ProbCmd):
        return AddExp(ScalExp(pgcl.probExpr, wp(pgcl.cmd1, g)), ScalExp(MinusExpr(IntNum(1), pgcl.probExpr), wp(pgcl.cmd2, g))) 
    elif isinstance(pgcl, IfElseCmd):
        return AddExp(GuardExp(pgcl.bexpr, wp(pgcl.cmdIf, g)), GuardExp(NegBexpr(pgcl.bexpr), wp(pgcl.cmdElse, g)))
    elif isinstance(pgcl, NonDetCmd):
        return MinExp(wp(pgcl.cmd1, g), wp(pgcl.cmd2, g))
    elif isinstance(pgcl, WhileCmd):
        modVars = getModifiedVars(pgcl.cmd, set())
        return InvGuard(InvIneq(AddExp(GuardExp(NegBexpr(pgcl.bexpr), g), GuardExp(pgcl.bexpr, wp(pgcl.cmd, pgcl.inv))), pgcl.inv, modVars), pgcl.inv)
    else :
        raise Exception("WP: not implemented for type" + pgcl)


def rightMostInv(g):
    if isinstance(g, InvIneq):
        return rightMostInv(g.inv)
    return g

def invCheck(g, solver, vars) :
    if isinstance(g, AExp) :
        return g
    elif isinstance(g, BExp) :
        return g
    elif isinstance(g, InvGuard) :
        newInvIneq =  invCheck(g.invIneq, solver, vars)

        if solver.lower() == "z3" :
            isSat = invCheckZ3(newInvIneq, vars)
        elif solver.lower() == "cvc5" :
            isSat = invCheckCVC5(newInvIneq, vars)
        else :
            raise Exception(solver + " is not a valid solver")
        if isSat :
            return g.inv
        else :
            if debug : 
                if isinstance(g.invIneq, InvIneq) :
                    print("Invalid invariant:")
                    print(prettify(g.invIneq.inv))
            raise Exception("Invalid invariant: " + prettify(g.invIneq.inv))
    elif isinstance(g, InvIneq) :
        return InvIneq (invCheck(g.lhs, solver, vars), g.inv, g.modVars)
    elif isinstance(g, MinExp) :
        return MinExp(invCheck(g.exp1, solver, vars), invCheck(g.exp2, solver, vars))
    elif isinstance(g, ScalExp) :
        return ScalExp(g.aexp, invCheck(g.exp, solver, vars))
    elif isinstance(g, AddExp) :
        return AddExp(invCheck(g.exp1, solver, vars), invCheck(g.exp2, solver, vars))
    elif isinstance(g, GuardExp) :
        return GuardExp(g.bexp, invCheck(g.exp, solver, vars))
    elif isinstance(g, Variable) :
        return g
    elif isinstance(g, Invariant) :
        return g
    elif isExpression(g) :
        return g
    else :
        print(g)
        raise Exception("invCheck: not implemented for " + str(type(g)))

def invCheckWithTime(g, solver, vars, runTime) :
    if isinstance(g, AExp) :
        return g, runTime
    elif isinstance(g, BExp) :
        return g, runTime
    elif isinstance(g, InvGuard) :
        newInvIneq, rt1 =  invCheckWithTime(g.invIneq, solver, vars, 0.0)

        invariantTimeStart = time.time()
        if solver.lower() == "z3" :
            isSat = invCheckZ3(newInvIneq, vars)
        elif solver.lower() == "cvc5" :
            isSat = invCheckCVC5(newInvIneq, vars)
        else :
            raise Exception(solver + " is not a valid solver")
        
        invariantTime = (time.time()-invariantTimeStart)

        if isSat :
            return g.inv, runTime+rt1+invariantTime
        else :
            if debug : 
                if isinstance(g.invIneq, InvIneq) :
                    print("Invalid invariant:")
                    print(prettify(g.invIneq.inv))
            raise Exception("Invalid invariant")
    elif isinstance(g, InvIneq) :
        invineq, rt1 = invCheckWithTime(g.lhs, solver, vars, 0.0)
        return InvIneq (invineq, g.inv, g.modVars), runTime+rt1
    elif isinstance(g, MinExp) :
        lhs, rt1 = invCheckWithTime(g.exp1, solver, vars, 0.0)
        rhs, rt2 = invCheckWithTime(g.exp2, solver, vars, 0.0)
        return MinExp(lhs, rhs), runTime+rt1+rt2
    elif isinstance(g, ScalExp) :
        rhs, rt1 = invCheckWithTime(g.exp, solver, vars, 0.0)
        return ScalExp(g.aexp, rhs), runTime+rt1
    elif isinstance(g, AddExp) :
        lhs, rt1 = invCheckWithTime(g.exp1, solver, vars, 0.0)
        rhs, rt2 = invCheckWithTime(g.exp2, solver, vars, 0.0)
        return AddExp(lhs, rhs), runTime+rt1+rt2
    elif isinstance(g, GuardExp) :
        rhs, rt1 = invCheckWithTime(g.exp, solver, vars, 0.0)
        return GuardExp(g.bexp, rhs), runTime+rt1
    elif isinstance(g, Variable) :
        return g, runTime
    elif isinstance(g, Invariant) :
        return g, runTime
    elif isExpression(g) :
        return g, runTime
    else :
        print(g)
        raise Exception("invCheck: not implemented for " + str(type(g)))

def multiplyGuardWithExp(guard, exp) :
    if isinstance(exp, AExp) :
        return GuardExp(guard, exp)
    elif isinstance(exp, BExp) :
        return ScalExp(guard, exp)
    elif isinstance(exp, Exp) :
        return multiplyGuardWithExp(guard, exp.exp)
    elif isinstance(exp, GuardExp) :
        newGuard = ScalExp(guard, exp.bexp)
        return multiplyGuardWithExp(newGuard, exp.exp)
    elif isinstance(exp, ScalExp) :
        return ScalExp(exp.aexp, multiplyGuardWithExp(guard, exp.exp))
    elif isinstance(exp, AddExp) :
        return AddExp(multiplyGuardWithExp(guard, exp.exp1), multiplyGuardWithExp(guard, exp.exp2))
    elif isinstance(exp, InvIneq) :
        lhs = GuardExp(guard, exp.lhs)
        rhs = GuardExp(guard, exp.inv)
        return InvIneq(lhs, rhs, exp.modVars)
    elif isinstance(exp, InvGuard) :
        return InvGuard(multiplyGuardWithExp(guard, exp.invIneq), GuardExp(guard, exp.inv))
    elif isinstance(exp, Invariant) :
        return GuardExp(guard, exp.inv)
    elif isExpression(exp) :
        return GuardExp(guard, exp)
    elif isinstance(exp, MinExp) :
        return MinExp(multiplyGuardWithExp(guard, exp.exp1), multiplyGuardWithExp(guard, exp.exp2))
    else :
        raise Exception("multiplyGuardWithExp not implented for " + str(type(exp)))

def multiplyGuards(g) :
    if isinstance(g, AExp) :
        return g
    elif isinstance(g, BExp) :
        return g
    elif isinstance(g, Exp) :
        return multiplyGuards(g.exp)
    elif isinstance(g, AddExp) :
        return AddExp(multiplyGuards(g.exp1), multiplyGuards(g.exp2))
    elif isinstance(g, GuardExp) :
        return multiplyGuardWithExp(g.bexp, g.exp)
    elif isinstance(g, MinExp) :
        return MinExp(multiplyGuards(g.exp1), multiplyGuards(g.exp2))
    elif isinstance(g, ScalExp) :
        if isinstance(g.exp, AExp) :
            return g
        elif isinstance(g.exp, BExp) :
            return multiplyGuardWithExp(g.exp, g.aexp)
        elif isinstance(g.exp, Exp) :
            return multiplyGuards(ScalExp(g.aexp, g.exp.exp))
        elif isinstance(g.exp, AddExp) :
            return g
        elif isinstance(g.exp, GuardExp) :
            return ScalExp(g.aexp, multiplyGuardWithExp(g.exp.bexp, g.exp.exp))
        elif isinstance(g.exp, ScalExp) :
            return ScalExp(g.aexp, ScalExp(g.exp.aexp, multiplyGuards(g.exp.exp)))
        elif isinstance(g.exp, InvGuard) :
            return g
        elif isExpression(g.exp) :
            return g
        else :
            return g
    elif isinstance(g, InvIneq) :
        return InvIneq(multiplyGuards(g.lhs), multiplyGuards(g.inv), g.modVars)
    elif isinstance(g, InvGuard) :
        return InvGuard(multiplyGuards(g.invIneq), multiplyGuards(g.inv))
    elif isinstance(g, Invariant) :
        return Invariant(multiplyGuards(g.inv))
    elif isExpression(g) :
        return g
    else :
        raise Exception("multiplyGuards not implemented for " + str(type(g)))


def isExpression(c) :
    if isinstance(c, (TimesExpr, DivExpr, PlusExpr, MinusExpr, DotMinusExpr, Expr, IntNum, RealNum, Variable, ProbExpr)) :
        return True
    else :
        return False
    
