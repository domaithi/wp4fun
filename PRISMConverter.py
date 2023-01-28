from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from Grammar.nodes.InitNodes import *
from Grammar.nodes.PGNodes import *
from WeakestPreexpectation import *

# Gloabal variable: Node counter
# Keeps track of the number of nodes/states in the Program Graph
nc = 1

def PGCmds (cmd, q1, q2) :
    global nc
    graph = []
    if isinstance(cmd, SkipCmd) :
        graph.append(PGEdge(q1,q2,cmd))
    elif isinstance(cmd, AssCmd) :
        return [PGEdge(q1,q2,cmd)]
    # Branches out (and merges back again)
    elif isinstance(cmd, UnifCmd) :
        probEdges = []
        denominator = cmd.upper-cmd.lower+1
        for i in range(cmd.lower, cmd.upper+1):
            nc += 1
            probEdges.append(PGEdge(q1, nc, ProbExpr(DivExpr(IntNum(1),IntNum(denominator)))))
            graph.append(PGEdge(nc, q2, AssCmd(cmd.var,IntNum(i))))
        graph.append(PGProbEdges(q1,probEdges))
    elif isinstance(cmd, ProbCmd) :
        probEdges = []
        # Handle the lhs 
        nc += 1
        probEdges.append(PGEdge(q1, nc, cmd.probExpr))
        graph += PGCmds(cmd.cmd1,nc,q2)
        # Handle the rhs
        nc += 1
        probEdges.append(PGEdge(q1, nc, ProbExpr(MinusExpr(IntNum(1),cmd.probExpr)))) 
        graph += PGCmds(cmd.cmd2,nc,q2)
        graph.append(PGProbEdges(q1, probEdges))
    elif isinstance(cmd, NonDetCmd) :
        # Handle the lhs 
        nc += 1
        graph.append(PGEdge(q1,nc,SkipCmd()))
        graph += PGCmds(cmd.cmd1,nc,q2)
        #Handle the rhs
        nc +=1
        graph.append(PGEdge(q1,nc,SkipCmd()))
        graph += PGCmds(cmd.cmd2,nc,q2)
    elif isinstance(cmd, IfElseCmd) :
        # Handle the if command
        nc += 1
        ncTemp = nc
        graph.append(PGEdge(q1,ncTemp,BExpr(cmd.bexpr)))
        graph += PGCmds(cmd.cmdIf, ncTemp, q2)
        # Handle the else command
        nc += 1
        ncTemp = nc
        graph.append(PGEdge(q1, ncTemp, BExpr(NegBexpr(cmd.bexpr))))
        graph += PGCmds(cmd.cmdElse, ncTemp, q2)
    elif isinstance(cmd, WhileCmd) :
        nc += 1
        ncTemp = nc
        graph.append(PGEdge(q1,ncTemp, BExpr(cmd.bexpr)))
        graph += PGCmds(cmd.cmd, ncTemp, q1)
        graph.append(PGEdge(q1, q2, BExpr(NegBexpr(cmd.bexpr))))
    elif isinstance(cmd,SeqCmd) :
        nc += 1
        ncTemp = nc
        graph += (PGCmds(cmd.cmd1,q1,nc)) + (PGCmds(cmd.cmd2, ncTemp, q2))
    return graph

def addSelfLopp(graph, q1, q2) :
    graph.append(PGEdge(q1,q2,SkipCmd()))
    graph.append(PGEdge(q2,q2,SkipCmd())) 
    return graph

def exprToString (e) :
    if isinstance(e, Expr) :
        return exprToString(e.expr)
    elif isinstance(e, Variable) : 
        return e.var.__str__()
    elif isinstance(e, IntNum) :
        return e.num.__str__()
    elif isinstance(e, RealNum) :
        return e.num.__str__()
    elif isinstance(e, ProbExpr) :
        return exprToString(e.expr)
    elif isinstance(e, TimesExpr) :
        return "(" + exprToString(e.expr1) + "*" + exprToString(e.expr2) + ")"
    elif isinstance(e, DivExpr) :
        return "(" + exprToString(e.expr1) + "/" + exprToString(e.expr2) + ")"
    elif isinstance(e, PlusExpr) :
        return "(" + exprToString(e.expr1) + "+" + exprToString(e.expr2) + ")"
    elif isinstance(e, MinusExpr) :
        return "(" + exprToString(e.expr1) + "-" + exprToString(e.expr2) + ")"
    elif isinstance(e, DotMinusExpr) :
        return "(" + exprToString(e.expr1) + "-" + exprToString(e.expr2) + ")"
    elif isinstance(e,BExpr):
        return exprToString(e.bexpr)
    elif isinstance(e, Boool):
        if (e.value) :
            return "true"
        return  "false"
    elif isinstance(e, NegBexpr):
        return "!(" + exprToString(e.bexpr) + ")"
    elif isinstance(e, AndBexpr):
        return "(" + exprToString(e.bexpr1) + "&" + exprToString(e.bexpr2) + ")"
    elif isinstance(e, OrBexpr):
        return "(" + exprToString(e.bexpr1) + "|" + exprToString(e.bexpr2) + ")"
    elif isinstance(e, EqBexpr):
        return "(" + exprToString(e.expr1) + "=" + exprToString(e.expr2) + ")"
    elif isinstance(e, NEqBexpr):
        return "(" + exprToString(e.expr1) + "!=" + exprToString(e.expr2) + ")"
    elif isinstance(e, GTBexpr):
        return "(" + exprToString(e.expr1) + ">" + exprToString(e.expr2) + ")"
    elif isinstance(e, LTBexpr):
        return "(" + exprToString(e.expr1) + "<" + exprToString(e.expr2) + ")"
    elif isinstance(e, GEqBexpr):
        return "(" + exprToString(e.expr1) + ">=" + exprToString(e.expr2) + ")"
    elif isinstance(e, LEqBexpr):
        return "(" + exprToString(e.expr1) + "<=" + exprToString(e.expr2) + ")"
    elif isinstance(e, AExp) :
        return exprToString(e.expr)
    elif isinstance(e, BExp) :
        return exprToString(e.bexpr)
    elif isinstance(e, AddExp) :
        return "(" + exprToString(e.exp1) + ") + (" + exprToString(e.exp2) + ")"
    elif isinstance(e, ScalExp) :
        return "(" + exprToString(e.aexp) + ") * (" + exprToString(e.exp) + ")" 
    elif isinstance(e, Invariant) :
        return exprToString(e.inv)  
    else : 
        raise Exception("ExprToString: not implemented yet: ", e)

def edgeToString (edge) :
    if isinstance(edge, PGProbEdges):
        s = "(pc="+ edge.start.__str__() +") -> "
        first = True
        for e in edge.edges:
            if isinstance(e, PGEdge) :
                if isinstance(e.action, ProbExpr) :
                    if (not(first)) :
                         s += " + " 
                    s += exprToString(e.action.expr) + ": (pc'=" + e.end.__str__() + ")"
                    first = False
            else :
                print(e)
        return s + ""
    if isinstance(edge, PGEdge) :
        action = edge.action
        if isinstance(action, SkipCmd) :
            return "(pc="+ edge.start.__str__() +") -> (pc'=" + edge.end.__str__() + ")"
        elif isinstance(action, AssCmd) :
            return "(pc="+ edge.start.__str__() +") -> (pc'=" + edge.end.__str__() + ") & (" + action.var.__str__() + "'=" + exprToString(action.expr) + ")"
        elif isinstance(action, BExpr) :
            return "(pc="+ edge.start.__str__() +") & ("+ exprToString(action.bexpr) +") -> (pc'=" + edge.end.__str__() + ")"
        else : # This should never happen
            raise Exception("printEdge-fail: ", edge.__str__())
    else : #This should never happen
        print("printEdge: input not of type PGEdge") 

def edgesToString (edges) :
    s = ""
    for e in (edges) :
        s += "[] " + edgeToString(e) + ";\n"
    return s

def initVars (init) :
    res = ""
    if isinstance(init, Init) :
        #if isinstance(init.range, Range)  and isinstance(init.var, VarInt) and isinstance(init.init, IntNum) :
        if isinstance(init.var, Variable) :
            res += init.var.var.__str__() + " : "
        if isinstance(init.range, Ranges) :
            res += "[" + init.range.start.__str__() + ".." + init.range.end.__str__() + "] " 
        if isinstance(init.init, IntNum) :
            res += "init " +  init.init.num.__str__() + ";\n"
    elif isinstance(init, InitSeqNode) :
        res = initVars(init.left) + initVars(init.right)
    else:
        raise Exception("initVars: not implemented yet")
    return res

def preToString(pre) :
    if isinstance(pre, Constraint) :
        return str(pre.op) + exprToString(pre.exp)

def toPrism (pgcl, pre, post, inits) :
    global nc
    nc = 1
    pg = PGCmds(pgcl, 0, 1)
    nc += 1
    pg = addSelfLopp(pg, 1, nc)
    body = edgesToString(pg)
    states = Init(Variable('pc'), Ranges(0,nc), IntNum(0))
    Post = exprToString(post)

    prism = "mdp\n\nmodule TestMDP" + "\n\n"
    prism += initVars(states)
    prism += initVars(inits) +"\n"
    prism += body
    prism += "\nendmodule\n"
    prism += "\nrewards \"post\"\n"
    prism += "\npc=1 : " + Post + ";\n"
    prism += "\nendrewards\n\n"

    props = "R{\"post\"}" + preToString(pre) +" [ F pc=" + nc.__str__() + " ]\n"
    return prism, props