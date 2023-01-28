class InitSeqNode():
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def __str__(self):
        return "InitSeq(" + self.left.__str__() + ", " + self.right.__str__() + ")"

    
class Init():
    def __init__(self, var=None, range=None, init=None):
        self.var = var
        self.range = range
        self.init = init
    def __str__(self):
        return "Init(" + self.var.__str__() + ", " + self.range.__str__() + ", " + self.init.__str__() + ")"

    
class Ranges():
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
    def __str__(self):
        return "Range(" + str(self.start) + ", " + str(self.end) + ")"

