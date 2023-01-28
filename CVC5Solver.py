from cvc5.pythonic import *
from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from GlobalVariables import *

def expToCVC5(e):
        # Expectations
    if isinstance(e, AExp) :
        return expToCVC5(e.expr)
    elif isinstance(e, BExp) :
        return If(expToCVC5(e.bexpr), 1, 0)
    elif isinstance(e, GuardExp) :
        return expToCVC5(e.bexp) * expToCVC5(e.exp)
    elif isinstance(e, AddExp) :
        return expToCVC5(e.exp1) + expToCVC5(e.exp2)
    elif isinstance(e, ScalExp) :
        return expToCVC5(e.aexp) * expToCVC5(e.exp)
    elif isinstance(e, MinExp) :
        lhs = expToCVC5(e.exp2)
        rhs = expToCVC5(e.exp1)
        return If(lhs > rhs, rhs, lhs)
    elif isinstance(e, Invariant) :
        return expToCVC5(e.inv)
    elif isinstance(e, Exp) :
        return expToCVC5(e.exp)
    elif isinstance(e, InvIneq):
        return expToCVC5(e.lhs) <= expToCVC5(e.inv)
    # AExpressions
    elif isinstance(e, IntNum) :
        if varIsOfReal :
            return RealVal(e.num)
        else :
            return IntVal(e.num)  
    elif isinstance(e, RealNum) : 
        return RealVal(e.num)
    elif isinstance(e, ProbExpr) :
        return expToCVC5(e.expr)
    elif isinstance(e, Variable) :
        if varIsOfReal :
            return Real(e.var)
        else :
            return Int(e.var)                                   
    elif isinstance(e, TimesExpr) :
        return expToCVC5(e.expr1) * expToCVC5(e.expr2)
    elif isinstance(e, DivExpr) :
        if isinstance(e.expr1, IntNum) and isinstance(e.expr2, IntNum):
            return Q(e.expr1.num, e.expr2.num)
        return expToCVC5(e.expr1) / expToCVC5(e.expr2)
    elif isinstance(e, PlusExpr) :
        return expToCVC5(e.expr1) + expToCVC5(e.expr2) 
    elif isinstance(e, MinusExpr) :
        return expToCVC5(e.expr1) - expToCVC5(e.expr2) 
    elif isinstance(e, DotMinusExpr) :
        lhs = expToCVC5(e.expr1)
        rhs = expToCVC5(e.expr2)
        return If(lhs > rhs, lhs - rhs, 0)
    elif isinstance(e, Expr):
        return expToCVC5(e.expr)
    elif isinstance(e, ForAllBexpr) :
        if varIsOfReal :
            newVars = [Real(var) for var in e.vars]
        else :
            newVars = [Int(var) for var in e.vars]
        return ForAll(newVars, expToCVC5(e.bexpr))
    # BExpressions
    elif isinstance(e, Boool) :
        return e.value
    elif isinstance(e, AndBexpr) :
        return And(expToCVC5(e.bexpr1), expToCVC5(e.bexpr2))
    elif isinstance(e, OrBexpr) :
        return Or(expToCVC5(e.bexpr1), expToCVC5(e.bexpr2))
    elif isinstance(e, NegBexpr) :
        return Not(expToCVC5(e.bexpr))
    elif isinstance(e, EqBexpr) :
        return expToCVC5(e.expr1) == expToCVC5(e.expr2)
    elif isinstance(e, NEqBexpr) :
        return expToCVC5(e.expr1) != expToCVC5(e.expr2)
    elif isinstance(e, GTBexpr) :
        return expToCVC5(e.expr1) > expToCVC5(e.expr2)
    elif isinstance(e, GEqBexpr) :
        return expToCVC5(e.expr1) >= expToCVC5(e.expr2)
    elif isinstance(e, LTBexpr) :
        return expToCVC5(e.expr1) < expToCVC5(e.expr2)
    elif isinstance(e, LEqBexpr) :
        return expToCVC5(e.expr1) <= expToCVC5(e.expr2)
    elif isinstance(e, ImpBexpr) :
        return Implies(expToCVC5(e.expr1), expToCVC5(e.expr2))
    # Cases for old WP:
    elif isinstance(e, int) :
        if varIsOfReal :
            return RealVal(e)
        else :
            return IntVal(e)  
    elif isinstance(e, float) :
        if varIsOfReal :
            return RealVal(e)
        else :
            return IntVal(e) 
    else :
        raise Exception("expToCVC5: not implemented for type " + str(type(e)))


def constraintToCVC5(g, cons):
    if isinstance(cons, Constraint):
        if (cons.op == "<") :
            return expToCVC5(g) < expToCVC5(cons.exp)
        elif (cons.op == "<=") :
            return expToCVC5(g) <= expToCVC5(cons.exp)
        elif (cons.op == ">") :
            return expToCVC5(g) > expToCVC5(cons.exp)
        elif (cons.op == ">=") :
            return expToCVC5(g) >= expToCVC5(cons.exp)
        elif (cons.op == "==" or cons.op == '=') :
            return expToCVC5(g) == expToCVC5(cons.exp)
        elif (cons.op == "!=") :
            return expToCVC5(g) != expToCVC5(cons.exp)
        else :
            raise Exception("constraintToCVC5: Not a valid operator:", cons.op)
    else :
        raise Exception("constraintToCVC5: Not a valid contraint:", cons)

def addVars(vars, slv):
    for var in vars:        
        if varIsOfReal :
            slv.add(Real(var) >= 0)
        else :
            slv.add(Int(var) >= 0)
            
def solveCVC5(g, constraint, vars) :
    s = Solver()
    s.reset()
    formula = constraintToCVC5(g, constraint)
    formula = simplify(formula)
    addVars(vars, s)
    s.add(Not(formula)) 
    result = s.check()
    if result == sat: 
        if debug and varIsOfReal :
           print("Model:", s.model()) 
        return False
    elif result == unsat:
        return True
    else:
        print(s.reason_unknown())
        raise Exception("solveCVC5: unknown sat result\n")

def invCheckCVC5(g, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = expToCVC5(g) 
    formula = simplify(formula)
    s.add(Not(formula)) 
    result = s.check()
    if result == sat :
        if debug and not varIsOfReal :
           print("Model:", s.model()) 
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("invCheckCVC5: unknown sat result\n")

def nonNegCVC5(nonNeg, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = Not(expToCVC5(nonNeg))
    s.add(formula)
    result = s.check()
    if result == sat :
        if debug and not varIsOfReal :
           print("Model:", s.model()) 
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("nonNegCVC5: unknown sat result\n")
    
def probCheckCVC5(probCheck, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = expToCVC5(probCheck)
    s.add(Not(formula))
    result = s.check()
    if result == sat :
        if debug and not varIsOfReal :
           print("Model:", s.model()) 
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("probCheckCVC5: unknown sat result\n")
