class Boool():
    def __init__(self, value=None):
        self.value = value
    def __str__(self):
        return "Bool(" + self.value.__str__() + ")"

class AndBexpr():
    def __init__(self, bexpr1=None, bexpr2=None):
        self.bexpr1 = bexpr1
        self.bexpr2 = bexpr2
    def __str__(self):
        return "And(" + self.bexpr1.__str__() + ", " + self.bexpr2.__str__() + ")"

class OrBexpr():
    def __init__(self, bexpr1=None, bexpr2=None):
        self.bexpr1 = bexpr1
        self.bexpr2 = bexpr2
    def __str__(self):
        return "Or(" + self.bexpr1.__str__() + ", " + self.bexpr2.__str__() + ")"

class NegBexpr():
    def __init__(self, bexpr=None):
        self.bexpr = bexpr
    def __str__(self):
        return "Neg(" + self.bexpr.__str__() + ")"

class EqBexpr(): #Equals
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "Eq(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"
        
class NEqBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "NEq(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class GTBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "GT(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class LTBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "LT(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class GEqBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "GEq(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"
        
class LEqBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "LEq(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class BExpr():
    def __init__(self, bexpr=None):
        self.bexpr = bexpr
    def __str__(self):
        return "BExpr(" + self.bexpr.__str__() + ")"

class ImpBexpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "Imp(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"
    

class ForAllBexpr():
    def __init__(self, vars=None, bexpr=None):
        self.vars = vars
        self.bexpr = bexpr
    def __str__(self):
        return "ForAll(" + self.vars.__str__() + ", " + self.bexpr.__str__() + ")"