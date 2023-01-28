class AExp():
    def __init__(self, expr=None):
        self.expr = expr
    def __str__(self):
        return "AExp(" + self.expr.__str__() + ")"

class BExp():
    def __init__(self, bexpr=None):
        self.bexpr = bexpr
    def __str__(self):
        return "BExp(" + self.bexpr.__str__() + ")"

class GuardExp():
    def __init__(self, bexp=None, exp=None):
        self.bexp = bexp
        self.exp = exp
    def __str__(self):
        return "GuardExp(" + self.bexp.__str__() + ", " + self.exp.__str__() + ")"
        
class AddExp():
    def __init__(self, exp1=None, exp2=None):
        self.exp1 = exp1
        self.exp2 = exp2
    def __str__(self):
        return "AddExp(" + self.exp1.__str__() + ", " + self.exp2.__str__() + ")"
        
class ScalExp():
    def __init__(self, aexp=None, exp=None):
        self.aexp = aexp
        self.exp = exp
    def __str__(self):
        return "ScalExp(" + self.aexp.__str__() + ", " + self.exp.__str__() + ")"
    
class MinExp():
    def __init__(self, exp1=None, exp2=None):
        self.exp1 = exp1
        self.exp2 = exp2
    def __str__(self):
        return "Min(" + self.exp1.__str__() + ", " + self.exp2.__str__() + ")"
class Exp():
    def __init__(self, exp=None):
        self.exp = exp
    def __str__(self):
        return "Exp(" + self.exp.__str__() + ")"
    
class InvIneq():
    def __init__(self, lhs=None, inv=None, modVars=None):
        self.lhs = lhs
        self.inv = inv
        self.modVars = modVars
    def __str__(self):
        return "InvIneq(" + self.lhs.__str__() + ", " + self.inv.__str__() + ", " + self.modVars.__str__() + ")"

class Invariant():
    def __init__(self, inv=None):
        self.inv = inv
    def __str__(self):
        return "Invariant[" + self.inv.__str__() + "]"
    
class Constraint():
    def __init__(self, op=None, exp=None):
        self.op = op
        self.exp = exp
    def __str__(self):
        return "Constraint(" + self.op.__str__() + ", " + self.exp.__str__() + ")"

class InvGuard():
    def __init__(self, invIneq=None, inv=None):
        self.invIneq = invIneq
        self.inv = inv
    def __str__(self):
        return "InvGuard(" + self.invIneq.__str__() + ", " + self.inv.__str__() + ")"