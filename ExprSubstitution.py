from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from GlobalVariables import * 
from ExtractVars import *

def exprSubstitutionWithModVars(g, x, e, modVars) :
    # Expectations
    if isinstance(g, AExp) :
        return AExp(exprSubstitutionWithModVars(g.expr, x, e, modVars))
    elif isinstance(g, BExp) :
        return BExp(exprSubstitutionWithModVars(g.bexpr, x, e, modVars))
    elif isinstance(g, GuardExp) :
        return GuardExp(exprSubstitutionWithModVars(g.bexp, x, e, modVars), exprSubstitutionWithModVars(g.exp, x, e, modVars))
    elif isinstance(g, AddExp) :
        return AddExp(exprSubstitutionWithModVars(g.exp1, x, e, modVars), exprSubstitutionWithModVars(g.exp2, x, e, modVars))
    elif isinstance(g, ScalExp) :
        return ScalExp(exprSubstitutionWithModVars(g.aexp, x, e, modVars), exprSubstitutionWithModVars(g.exp, x, e, modVars))
    elif isinstance(g, MinExp) :
        return MinExp(exprSubstitutionWithModVars(g.exp2, x, e, modVars), exprSubstitutionWithModVars(g.exp1, x, e, modVars))
    elif isinstance(g, Invariant):
        return exprSubstitutionWithModVars(g.inv, x, e, modVars)
    elif isinstance(g, Exp) :
        return exprSubstitutionWithModVars(g.exp, x, e, modVars)
    elif isinstance(g, InvIneq):
        mv = modVars.union(g.modVars)
        return InvIneq(exprSubstitutionWithModVars(g.lhs, x, e, mv.copy()), exprSubstitutionWithModVars(g.inv, x, e, mv.copy()), mv.copy()) 
    elif isinstance(g, InvGuard):
        return InvGuard(exprSubstitutionWithModVars(g.invIneq, x, e, modVars), exprSubstitutionWithModVars(g.inv, x, e, modVars), modVars) 
    # AExpressions
    elif isinstance(g, IntNum) :
        return g
    elif isinstance(g, RealNum) :
        return g
    elif isinstance(g, ProbExpr) :
        return ProbExpr(exprSubstitutionWithModVars(g.expr, x, e, modVars))
    elif isinstance(g, Variable) :
        expVars = extractVariables(e, set())      
        if (g.var == x) and (g.var not in modVars) and (not expVars.intersection(modVars)) :
            return e
        else :
            return g
    elif isinstance(g, TimesExpr) :
        return TimesExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, DivExpr) :
        return DivExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, PlusExpr) :
        return PlusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, MinusExpr) :
        return MinusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, DotMinusExpr) :
        return DotMinusExpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    # BExpressions
    elif isinstance(g, Boool) :
        return g
    elif isinstance(g, NegBexpr) :
        return NegBexpr(exprSubstitutionWithModVars(g.bexpr, x, e, modVars))
    elif isinstance(g, AndBexpr) :
        return AndBexpr(exprSubstitutionWithModVars(g.bexpr1, x, e, modVars), exprSubstitutionWithModVars(g.bexpr2, x, e, modVars))
    elif isinstance(g, OrBexpr) :
        return OrBexpr(exprSubstitutionWithModVars(g.bexpr1, x, e, modVars), exprSubstitutionWithModVars(g.bexpr2, x, e, modVars))
    elif isinstance(g, EqBexpr) :
        return EqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, NEqBexpr) :
        return NEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, GEqBexpr) :
        return GEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, GTBexpr) :
        return GTBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, LEqBexpr) :
        return LEqBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, LTBexpr) :
        return LTBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, Expr):
        return exprSubstitutionWithModVars(g.expr, x, e, modVars)
    elif isinstance(g, ImpBexpr):
        return ImpBexpr(exprSubstitutionWithModVars(g.expr1, x, e, modVars), exprSubstitutionWithModVars(g.expr2, x, e, modVars))
    elif isinstance(g, ForAllBexpr):
        if x not in g.vars :
            return ForAllBexpr(g.vars, exprSubstitutionWithModVars(g.bexpr))
        return g
    # Case used for old wp
    elif isinstance(g, int) :
        return IntNum(g)
    else :
        print("\nG = ", g, '\n')
        raise Exception("exprSubstitutionWithModVars: Not implemented for type", g)
    

def exprSubstitution(g, x, e) :
    # Expectations
    if isinstance(g, AExp) :
        return AExp(exprSubstitution(g.expr, x, e))
    elif isinstance(g, BExp) :
        return BExp(exprSubstitution(g.bexpr, x, e))
    elif isinstance(g, GuardExp) :
        return GuardExp(exprSubstitution(g.bexp, x, e), exprSubstitution(g.exp, x, e))
    elif isinstance(g, AddExp) :
        return AddExp(exprSubstitution(g.exp1, x, e), exprSubstitution(g.exp2, x, e))
    elif isinstance(g, ScalExp) :
        return ScalExp(exprSubstitution(g.aexp, x, e), exprSubstitution(g.exp, x, e))
    elif isinstance(g, MinExp) :
        return MinExp(exprSubstitution(g.exp2, x, e), exprSubstitution(g.exp1, x, e))
    elif isinstance(g, Invariant):
        return exprSubstitution(g.inv, x, e)
    elif isinstance(g, Exp) :
        return exprSubstitution(g.exp, x, e)
    elif isinstance(g, InvIneq):
        return InvIneq(exprSubstitution(g.lhs, x, e), exprSubstitution(g.inv, x, e), g.modVars) 
    # AExpressions
    elif isinstance(g, IntNum) :
        return g
    elif isinstance(g, RealNum) :
        return g
    elif isinstance(g, ProbExpr) :
        return ProbExpr(exprSubstitution(g.expr, x, e))
    elif isinstance(g, Variable) :
        if g.var == x :
            return e
        else :
            return g
    elif isinstance(g, TimesExpr) :
        return TimesExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, DivExpr) :
        return DivExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, PlusExpr) :
        return PlusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, MinusExpr) :
        return MinusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, DotMinusExpr) :
        return DotMinusExpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    # BExpressions
    elif isinstance(g, Boool) :
        return g
    elif isinstance(g, NegBexpr) :
        return NegBexpr(exprSubstitution(g.bexpr, x, e))
    elif isinstance(g, AndBexpr) :
        return AndBexpr(exprSubstitution(g.bexpr1, x, e), exprSubstitution(g.bexpr2, x, e))
    elif isinstance(g, OrBexpr) :
        return OrBexpr(exprSubstitution(g.bexpr1, x, e), exprSubstitution(g.bexpr2, x, e))
    elif isinstance(g, EqBexpr) :
        return EqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, NEqBexpr) :
        return NEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, GEqBexpr) :
        return GEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, GTBexpr) :
        return GTBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, LEqBexpr) :
        return LEqBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, LTBexpr) :
        return LTBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, Expr):
        return exprSubstitution(g.expr, x, e)
    elif isinstance(g, ImpBexpr):
        return ImpBexpr(exprSubstitution(g.expr1, x, e), exprSubstitution(g.expr2, x, e))
    elif isinstance(g, ForAllBexpr):
        expVars = extractVariables(e, set()) 
        if (x not in g.vars) and (not expVars.intersection(set(g.vars))) :
            return ForAllBexpr(g.vars, exprSubstitution(g.bexpr, x, e))
        return g
    # Case used for old wp
    elif isinstance(g, int) :
        return IntNum(g)
    else :
        print("\nG = ", g, '\n')
        raise Exception("exprSubstitution: Not implemented for type", g)
    

############ GET MODIFIED VARIABLES IN LOOP BODY ############

def getModifiedVars(pgcl, acc) :
    if isinstance(pgcl, SkipCmd) :
        return acc
    elif isinstance(pgcl, AssCmd):
        acc.add(pgcl.var)
        return acc
    elif isinstance(pgcl, UnifCmd):
        acc.add(pgcl.var)
        return acc
    elif isinstance(pgcl, SeqCmd):
        return getModifiedVars(pgcl.cmd1, acc).union(getModifiedVars(pgcl.cmd2, acc))
    elif isinstance(pgcl, ProbCmd):
        return getModifiedVars(pgcl.cmd1, acc).union(getModifiedVars(pgcl.cmd2, acc))
    elif isinstance(pgcl, IfElseCmd):
        return getModifiedVars(pgcl.cmdIf, acc).union(getModifiedVars(pgcl.cmdElse, acc))
    elif isinstance(pgcl, NonDetCmd):
        return getModifiedVars(pgcl.cmd1, acc).union(getModifiedVars(pgcl.cmd2, acc))
    elif isinstance(pgcl, WhileCmd):
        return getModifiedVars(pgcl.cmd, acc)
    else :
        print(pgcl)
        raise Exception("getModifiedVars: not implemented for type" + pgcl.__str__())


def varsShouldBeNonNeg(vars) :
    if len(vars) == 0 :
        return vars
    elif len(vars) == 1 :
        var = vars.pop()
        return GEqBexpr(Variable(var), IntNum(0))
    else :
        var = vars.pop()
        return AndBexpr(GEqBexpr(Variable(var), IntNum(0)), (varsShouldBeNonNeg(vars)))