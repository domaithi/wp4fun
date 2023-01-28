from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from z3 import *
from PrettyPrinter import *
from GlobalVariables import *

def expToZ3(e) :
    # Expectations
    if isinstance(e, AExp) :
        return expToZ3(e.expr)
    elif isinstance(e, BExp) :
        return If(expToZ3(e.bexpr), 1, 0)
    elif isinstance(e, GuardExp) :
        return (expToZ3(e.bexp) * expToZ3(e.exp))
    elif isinstance(e, AddExp) :
        return (expToZ3(e.exp1) + expToZ3(e.exp2))
    elif isinstance(e, ScalExp) :
        return (expToZ3(e.aexp) * expToZ3(e.exp))
    elif isinstance(e, MinExp) :
        lhs = expToZ3(e.exp1)
        rhs = expToZ3(e.exp2)
        return If(lhs > rhs, rhs, lhs)
    elif isinstance(e, Invariant) :
        return expToZ3(e.inv)
    elif isinstance(e, Exp) :
        return expToZ3(e.exp)
    elif isinstance(e, InvIneq):
        return expToZ3(e.lhs) <= expToZ3(e.inv)
    # AExpressions
    elif isinstance(e, IntNum) :
        if varIsOfReal :
            return RealVal(e.num)
        else :
            return IntVal(e.num)  
    elif isinstance(e, RealNum) :
        return RealVal(e.num)
    elif isinstance(e, ProbExpr) :
        return expToZ3(e.expr)
    elif isinstance(e, Variable) :
        if varIsOfReal :
            return Real(e.var)
        else :
            return Int(e.var)                               
    elif isinstance(e, TimesExpr) :
        return expToZ3(e.expr1) * expToZ3(e.expr2)
    elif isinstance(e, DivExpr) :
        if isinstance(e.expr1, IntNum) and isinstance(e.expr2, IntNum):
            return Q(e.expr1.num, e.expr2.num)
        return expToZ3(e.expr1) / expToZ3(e.expr2)         
    elif isinstance(e, PlusExpr) :
        return expToZ3(e.expr1) + expToZ3(e.expr2) 
    elif isinstance(e, MinusExpr) :
        return expToZ3(e.expr1) - expToZ3(e.expr2) 
    elif isinstance(e, DotMinusExpr) :
        lhs = expToZ3(e.expr1)
        rhs = expToZ3(e.expr2)
        return If(lhs > rhs, lhs - rhs, 0)
    elif isinstance(e, Expr):
        return expToZ3(e.expr)
    # BExpressions
    elif isinstance(e, Boool) :
        return e.value
    elif isinstance(e, AndBexpr) :
        return And(expToZ3(e.bexpr1), expToZ3(e.bexpr2))
    elif isinstance(e, OrBexpr) :
        return Or(expToZ3(e.bexpr1), expToZ3(e.bexpr2))
    elif isinstance(e, NegBexpr) :
        return Not(expToZ3(e.bexpr))
    elif isinstance(e, EqBexpr) :
        return expToZ3(e.expr1) == expToZ3(e.expr2)
    elif isinstance(e, NEqBexpr) :
        return expToZ3(e.expr1) != expToZ3(e.expr2)
    elif isinstance(e, GTBexpr) :
        return expToZ3(e.expr1) > expToZ3(e.expr2)
    elif isinstance(e, GEqBexpr) :
        return expToZ3(e.expr1) >= expToZ3(e.expr2)
    elif isinstance(e, LTBexpr) :
        return expToZ3(e.expr1) < expToZ3(e.expr2)
    elif isinstance(e, LEqBexpr) :
        return expToZ3(e.expr1) <= expToZ3(e.expr2)
    elif isinstance(e, ImpBexpr) :
        return Implies(expToZ3(e.expr1), expToZ3(e.expr2))
    elif isinstance(e, ForAllBexpr) :
        if varIsOfReal :
            newVars = [Real(var) for var in e.vars]
        else :
            newVars = [Int(var) for var in e.vars]
        return ForAll(newVars, expToZ3(e.bexpr))
    # Cases for old WP:
    elif isinstance(e, int) :
        if varIsOfReal :
            return RealVal(e)
        else :
            return IntVal(e)  
    elif isinstance(e, float) :
        return RealVal(e)
    else :
        raise Exception("expToZ3: not implemented for type " + str(type(e)))
        

def constraintToZ3(g, cons) :
    if isinstance(cons, Constraint):
        if (cons.op == "<") :
            return expToZ3(g) < expToZ3(cons.exp)
        elif (cons.op == "<=") :
            return expToZ3(g) <= expToZ3(cons.exp)
        elif (cons.op == ">") :
            return expToZ3(g) > expToZ3(cons.exp)
        elif (cons.op == ">=") :
            return expToZ3(g) >= expToZ3(cons.exp)
        elif (cons.op == "==" or cons.op == '=') :
            return expToZ3(g) == expToZ3(cons.exp)
        elif (cons.op == "!=") :
            return expToZ3(g) != expToZ3(cons.exp)
        else :
            raise Exception("constraintToZ3: Not a valid operator:", cons.op)
    else :
        raise Exception("constraintToZ3: Not a valid contraint:", cons)
            
def addVars(vars, slv):
    for var in vars:        
        if varIsOfReal :
            slv.add(Real(var) >= 0)
        else :
            slv.add(Int(var) >= 0)
            
def solveZ3(g, constraint, vars) :
    s = Solver()
    s.reset()
    formula = constraintToZ3(g,constraint) 
    formula = simplify(formula)
    addVars(vars, s)
    s.add(Not(formula)) 
    result = s.check()
    if result == sat :
        if debug :
            print("Model:", s.model())
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("solveZ3: unknown sat result\n")  
    
def invCheckZ3(g, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = expToZ3(g) 
    formula = simplify(formula)
    s.add(Not(formula)) 
    result = s.check()
    if result == sat :
        print("Model:", s.model())
        if debug :
            print("Model:", s.model())
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("invCheckZ3: unknown sat result\n")


def nonNegZ3(nonNeg, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = Not(expToZ3(nonNeg))
    s.add(formula)
    result = s.check()
    if result == sat :
        if debug :
            print("Model:", s.model())
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("nonNegZ3: unknown sat result\n")
    
def probCheckZ3(probCheck, vars) :
    s = Solver()
    s.reset()
    addVars(vars, s)
    formula = expToZ3(probCheck)
    s.add(Not(formula))
    result = s.check()
    if result == sat :
        if debug :
            print("Model:", s.model())
        return False
    elif result == unsat :
        return True
    else:
        print(s.reason_unknown())
        raise Exception("probCheckZ3: unknown sat result\n")
