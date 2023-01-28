class TimesExpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "TimesExpr(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class DivExpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "DivExpr(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class PlusExpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "PlusExpr(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class MinusExpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "MinusExpr(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class DotMinusExpr():
    def __init__(self, expr1=None, expr2=None):
        self.expr1 = expr1
        self.expr2 = expr2
    def __str__(self):
        return "DotMinusExpr(" + self.expr1.__str__() + ", " + self.expr2.__str__() + ")"

class Expr():
    def __init__(self, expr=None):
        self.expr = expr
    def __str__(self):
        return "Expr(" + self.expr.__str__() + ")"

class IntNum():
    def __init__(self, num=None):
        self.num = num
    def __str__(self):
        return "IntNum(" + str(self.num) + ")"
    
class RealNum():
    def __init__(self, num=None):
        self.num = num
    def __str__(self):
        return "RealNum(" + self.num + ")"

class Variable():
    def __init__(self, var=None):
        self.var = var
    def __str__(self):
        return "Variable(" + self.var + ")"

class ProbExpr():
    def __init__(self, expr=None):
        self.expr = expr
    def __str__(self):
        return "Prob[" + self.expr.__str__() + "]"
    