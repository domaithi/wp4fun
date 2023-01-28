class PGEdge():
    def __init__(self, start=None, end=None, action=None):
        self.start = start
        self.end = end
        self.action = action
    def __str__(self):
        return "PGEdge(" + self.start.__str__() + ", " + self.end.__str__() + ", " + self.action.__str__() + ")"

class PGProbEdges():
    def __init__(self, start=None, edges=None):
        self.start = start
        self.edges = edges
    def __str__(self):
        return "PGEdge(" + self.start.__str__() + ", " + self.edges.__str__() + ")"