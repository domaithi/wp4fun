class AssCmd():
    def __init__(self, var=None, expr=None):
        self.var = var
        self.expr = expr
    def __str__(self):
        return "AssCmd(" + self.var + ", " + self.expr.__str__() + ")"
    
class UnifCmd():
    def __init__(self, var=None, lower=None, upper=None):
        self.var = var
        self.lower = lower
        self.upper = upper
    def __str__(self):
        return "UnifCmdNode(" + self.var.__str__() + ", " + self.lower.__str__() + ".." + self.upper.__str__() + ")"

class SkipCmd():
    def __init__(self):
        self
    def __str__(self):
        return "SkipCmd"

class SeqCmd():
    def __init__(self, cmd1=None, cmd2=None):
        self.cmd1 = cmd1
        self.cmd2 = cmd2
    def __str__(self):
        return "SeqCmd(" + self.cmd1.__str__() + ", " + self.cmd2.__str__() + ")"
    
class ProbCmd():
    def __init__(self, cmd1=None, probExpr=None, cmd2=None):
        self.cmd1 = cmd1
        self.probExpr = probExpr
        self.cmd2 = cmd2
    def __str__(self):
        return "ProbCmd(" + self.cmd1.__str__() + ", " + self.probExpr.__str__() + ", " + self.cmd2.__str__() + ")"

class NonDetCmd():
    def __init__(self, cmd1=None, cmd2=None):
        self.cmd1 = cmd1
        self.cmd2 = cmd2
    def __str__(self):
        return "NonDetCmd(" + self.cmd1.__str__() + ", " + self.cmd2.__str__() + ")"

class IfElseCmd():
    def __init__(self, bexpr=None, cmdIf=None, cmdElse=None):
        self.bexpr = bexpr
        self.cmdIf = cmdIf
        self.cmdElse = cmdElse
    def __str__(self):
        return "IfElseCmd(" + self.bexpr.__str__() + ", " + self.cmdIf.__str__() + ", " + self.cmdElse.__str__() + ")"

class WhileCmd():
    def __init__(self, bexpr=None, inv=None, cmd=None):
        self.bexpr = bexpr
        self.inv  = inv
        self.cmd = cmd
    def __str__(self):
        return "WhileCmd(" + self.bexpr.__str__() + ", " + self.inv.__str__() + ", " + self.cmd.__str__() + ")"