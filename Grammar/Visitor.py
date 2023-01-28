from Grammar.dist.GrammarLexer import GrammarLexer
from Grammar.dist.GrammarParser import GrammarParser
from Grammar.dist.GrammarVisitor import GrammarVisitor
from Grammar.nodes.BExprNodes import *
from Grammar.nodes.ExprNodes import *
from Grammar.nodes.CmdNodes import *
from Grammar.nodes.ExpNodes import *
from Grammar.nodes.InitNodes import *

class Visitor(GrammarVisitor):
    ########### EXPRESSIONS ##########
    def visitMultDivExpr(self, ctx: GrammarParser.MultDivExprContext):
        expr1 = self.visit(ctx.expr1)
        expr2 = self.visit(ctx.expr2)
        op = ctx.op.text
        if (op == '*') :
            return TimesExpr(expr1, expr2)
        elif (op == '/') :
            return DivExpr(expr1, expr2)
        else :
            raise Exception("visitMultDivExpr: wrong operator " + op)

    def visitPlusMinusDotminusExpr(self, ctx: GrammarParser.PlusMinusDotminusExprContext):
        expr1 = self.visit(ctx.expr1)
        expr2 = self.visit(ctx.expr2)
        op = ctx.op.text
        if (op == '+') :
            return PlusExpr(expr1, expr2)
        elif (op == '-') :
            return MinusExpr(expr1, expr2)
        elif (op == '.-') :
            return DotMinusExpr(expr1, expr2)
        else :
            raise Exception("visitPlusMinusDotminusExpr: wrong operator " + op)
    
    def visitExpr(self, ctx:GrammarParser.ExprContext):
        expr = self.visit(ctx.expr)
        return Expr(expr)

    def visitIntExpr(self, ctx:GrammarParser.IntExprContext):
        num = int(ctx.num.text)
        return IntNum(num)

    def visitVarExpr(self, ctx:GrammarParser.VarExprContext):
        var = ctx.var.text
        return Variable(var)
    
    ########### BEXPRESSIONS ###########

    def visitBoolExpr(self, ctx:GrammarParser.BoolExprContext):
        val = ctx.val.text
        if val == "true":
            return Boool(True)
        else:
            return Boool(False)

    def visitAndExpr(self, ctx:GrammarParser.AndExprContext):
        bexpr1 = self.visit(ctx.bexpr1)
        bexpr2 = self.visit(ctx.bexpr2)
        return AndBexpr(bexpr1, bexpr2)

    def visitOrExpr(self, ctx:GrammarParser.OrExprContext):
        bexpr1 = self.visit(ctx.bexpr1)
        bexpr2 = self.visit(ctx.bexpr2)
        return OrBexpr(bexpr1, bexpr2)

    def visitNegExpr(self, ctx:GrammarParser.NegExprContext):
        bexpr = self.visit(ctx.bexpr)
        return NegBexpr(bexpr)

    def visitCompareExpr(self, ctx:GrammarParser.CompareExprContext):
        bexpr1 = self.visit(ctx.bexpr1)
        bexpr2 = self.visit(ctx.bexpr2)
        operator = ctx.op.text

        if operator == '=':
            return EqBexpr(bexpr1,bexpr2)
        elif operator == "!=":
            return NEqBexpr(bexpr1,bexpr2)
        elif operator == ">":
            return GTBexpr(bexpr1,bexpr2)
        elif operator == "<":
            return LTBexpr(bexpr1,bexpr2)
        elif operator == ">=":
            return GEqBexpr(bexpr1,bexpr2)
        elif operator == "<=":
            return LEqBexpr(bexpr1,bexpr2)

    def visitBExpr(self, ctx:GrammarParser.BExprContext):
        value = self.visit(ctx.bexpr)
        return BExpr(value)


    ########### COMMANDS ###########
    def visitAssCmd(self, ctx:GrammarParser.AssCmdContext):
        var = ctx.var.text
        expr = self.visit(ctx.expr)
        return AssCmd(var, expr)
        
    def visitUnifCmd(self, ctx:GrammarParser.UnifCmdContext):
        var = ctx.var
        lower = int(ctx.lower.text)
        upper = int(ctx.upper.text)
        if upper <= lower :
            raise Exception("visitUnifCmd: upper bound must be greater than lower bound in unif")
        return UnifCmd(var.text, lower, upper)

    def visitSkipCmd(self, ctx:GrammarParser.SkipCmdContext):
        return SkipCmd()

    def visitSeqCmd(self, ctx:GrammarParser.SeqCmdContext):
        cmd1 = self.visit(ctx.cmd1)
        cmd2 = self.visit(ctx.cmd2)
        if cmd2 is None:
            raise Exception("Parse error: Sequence should not end with the token ';' ")
        return SeqCmd(cmd1, cmd2)

    def visitProbCmd(self, ctx:GrammarParser.ProbCmdContext):
        probExpr = self.visit(ctx.expr)
        cmd1 = self.visit(ctx.cmd1)
        cmd2 = self.visit(ctx.cmd2)
        return ProbCmd(cmd1, ProbExpr(probExpr), cmd2)

    def visitNonDetCmd(self, ctx:GrammarParser.NonDetCmdContext):
        cmd1 = self.visit(ctx.cmd1)
        cmd2 = self.visit(ctx.cmd2)
        return NonDetCmd(cmd1, cmd2)

    def visitIfElseCmd(self, ctx:GrammarParser.IfElseCmdContext):
        condition = self.visit(ctx.bexpr)
        cmdIf = self.visit(ctx.cmdIf)
        cmdElse = self.visit(ctx.cmdElse)
        return IfElseCmd(condition, cmdIf, cmdElse)

    def visitWhileCmd(self, ctx:GrammarParser.WhileCmdContext):
        condition = self.visit(ctx.bexpr)
        invariant = Invariant(self.visit(ctx.inv))
        cmd = self.visit(ctx.cmd)
        return WhileCmd(condition, invariant, cmd)
    
    
    ########### AEXPRESSIONS EXPECTATION ###########
    def visitMultDivAExp(self, ctx: GrammarParser.MultDivAExpContext):
        aexp1 = self.visit(ctx.aexp1)
        aexp2 = self.visit(ctx.aexp2)
        op = ctx.op.text
        if (op == '*') :
            return TimesExpr(aexp1, aexp2)
        elif (op == '/') :
            return DivExpr(aexp1, aexp2)
        else : 
            raise Exception("visitMultDivAExp: wrong operator " + op)

    def visitPlusMinusDotminusAExp(self, ctx: GrammarParser.PlusMinusDotminusAExpContext):
        aexp1 = self.visit(ctx.aexp1)
        aexp2 = self.visit(ctx.aexp2)
        op = ctx.op.text
        if (op == '+') :
            return PlusExpr(aexp1, aexp2)
        elif (op == '-') :
            return MinusExpr(aexp1, aexp2)
        elif (op == '.-') :
            return DotMinusExpr(aexp1, aexp2)
        else :
            raise Exception("visitPlusMinusDotminusAExp: wrong operator " + op)

    def visitExprAExp(self, ctx:GrammarParser.ExprAExpContext):
        aexp = self.visit(ctx.aexp)
        return Expr(aexp)
    
    def visitRealAExp(self, ctx:GrammarParser.RealAExpContext):
        number = ctx.num.text
        return RealNum(number)
    
    def visitIntAExp(self, ctx:GrammarParser.IntAExpContext):
        number = int(ctx.num.text)
        return IntNum(number)
    
    def visitVarAExp(self, ctx:GrammarParser.VarAExpContext):
        var = ctx.var.text
        return Variable(var)
    
    def visitExprAExpPar(self, ctx:GrammarParser.ExprAExpParContext):
        aexp = self.visit(ctx.aexp)
        return Expr(aexp)
    
    def visitRealAExpPar(self, ctx:GrammarParser.RealAExpParContext):
        number = ctx.num.text
        return RealNum(number)
    
    def visitIntAExpPar(self, ctx:GrammarParser.IntAExpParContext):
        number = int(ctx.num.text)
        return IntNum(number)
    
    def visitVarAExpPar(self, ctx:GrammarParser.VarAExpParContext):
        var = ctx.var.text
        return Variable(var)
    
    
    ########### BEXPRESSIONS EXPECTATION ###########

    def visitBoolAExp(self, ctx:GrammarParser.BoolAExpContext):
        val = ctx.val.text
        if val == "true":
            return Boool(True)
        elif val == "false":
            return Boool(False)
        else:
            raise Exception("visitBoolAExp: unknown boolean " + val)

    def visitAndAExp(self, ctx:GrammarParser.AndAExpContext):
        bexp1 = self.visit(ctx.bexp1)
        bexp2 = self.visit(ctx.bexp2)
        return AndBexpr(bexp1, bexp2)

    def visitOrAExp(self, ctx:GrammarParser.OrAExpContext):
        bexp1 = self.visit(ctx.bexp1)
        bexp2 = self.visit(ctx.bexp2)
        return OrBexpr(bexp1, bexp2)

    def visitNegAExp(self, ctx:GrammarParser.NegAExpContext):
        bexp = self.visit(ctx.bexp)
        return NegBexpr(bexp)

    def visitCompareExp(self, ctx:GrammarParser.CompareExpContext):
        bexp1 = self.visit(ctx.bexp1)
        bexp2 = self.visit(ctx.bexp2)
        operator = ctx.op.text

        if operator == '=':
            return EqBexpr(bexp1,bexp2)
        elif operator == "!=":
            return NEqBexpr(bexp1,bexp2)
        elif operator == ">":
            return GTBexpr(bexp1,bexp2)
        elif operator == "<":
            return LTBexpr(bexp1,bexp2)
        elif operator == ">=":
            return GEqBexpr(bexp1,bexp2)
        elif operator == "<=":
            return LEqBexpr(bexp1,bexp2)

    def visitBAExp(self, ctx:GrammarParser.BAExpContext):
        bexp = self.visit(ctx.bexp)
        return BExpr(bexp)
    
    
    ########### EXPECTATION ###########
    def visitAExp(self, ctx:GrammarParser.AExpContext):
        aexp = self.visit(ctx.aexp)
        return AExp(aexp)
    
    def visitBExp(self, ctx:GrammarParser.BExpContext):
        bexp = self.visit(ctx.bexp)
        return BExp(bexp)
    
    def visitGuardExp(self, ctx:GrammarParser.GuardExpContext):
        bexp = self.visit(ctx.bexp)
        exp = self.visit(ctx.exp)
        return GuardExp(bexp, exp)
    
    def visitAddExp(self, ctx:GrammarParser.AddExpContext):
        exp1 = self.visit(ctx.exp1)
        exp2 = self.visit(ctx.exp2)
        return AddExp(exp1, exp2)
    
    def visitScalExp(self, ctx:GrammarParser.ScalExpContext):
        aexp = self.visit(ctx.aexp)
        exp = self.visit(ctx.exp)
        return ScalExp(aexp, exp)
    
    def visitCons(self, ctx:GrammarParser.ConsContext):
        op = ctx.op.text
        exp = self.visit(ctx.exp)
        return Constraint(op, exp)
    
    def visitExp(self, ctx:GrammarParser.ExpContext):
        exp = self.visit(ctx.exp)
        return Exp(exp)
    
    ########### INITIALIZATION ###########
    def visitInit(self, ctx:GrammarParser.InitContext):
        var = Variable(ctx.var.text)
        range = Ranges(int(ctx.start.text), int(ctx.end.text))
        init = IntNum(int(ctx.init.text))
        return Init(var, range, init)

    def visitInitSeq(self, ctx:GrammarParser.InitSeqContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return InitSeqNode(left, right)
    
    
    ########### HEADER ###########
    def visitPreExpectation(self, ctx:GrammarParser.PreExpectationContext):
        return self.visit(ctx.cons)
    
    def visitPostExpectation(self, ctx:GrammarParser.PostExpectationContext):
        return self.visit(ctx.exp)
    
    def visitInitializations(self, ctx:GrammarParser.InitializationsContext):
        return self.visit(ctx.init)
    
    def visitPGCLProgram(self, ctx:GrammarParser.PGCLProgramContext):
        return self.visit(ctx.cmd)