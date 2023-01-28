# Generated from Grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#PGCLProgram.
    def visitPGCLProgram(self, ctx:GrammarParser.PGCLProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PostExpectation.
    def visitPostExpectation(self, ctx:GrammarParser.PostExpectationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PreExpectation.
    def visitPreExpectation(self, ctx:GrammarParser.PreExpectationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Initializations.
    def visitInitializations(self, ctx:GrammarParser.InitializationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#MultDivExpr.
    def visitMultDivExpr(self, ctx:GrammarParser.MultDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PlusMinusDotminusExpr.
    def visitPlusMinusDotminusExpr(self, ctx:GrammarParser.PlusMinusDotminusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Expr.
    def visitExpr(self, ctx:GrammarParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#VarExpr.
    def visitVarExpr(self, ctx:GrammarParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#IntExpr.
    def visitIntExpr(self, ctx:GrammarParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#VarAExp.
    def visitVarAExp(self, ctx:GrammarParser.VarAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ExprAExp.
    def visitExprAExp(self, ctx:GrammarParser.ExprAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#PlusMinusDotminusAExp.
    def visitPlusMinusDotminusAExp(self, ctx:GrammarParser.PlusMinusDotminusAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#IntAExp.
    def visitIntAExp(self, ctx:GrammarParser.IntAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#RealAExp.
    def visitRealAExp(self, ctx:GrammarParser.RealAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#MultDivAExp.
    def visitMultDivAExp(self, ctx:GrammarParser.MultDivAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AndExpr.
    def visitAndExpr(self, ctx:GrammarParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BoolExpr.
    def visitBoolExpr(self, ctx:GrammarParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BExpr.
    def visitBExpr(self, ctx:GrammarParser.BExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#CompareExpr.
    def visitCompareExpr(self, ctx:GrammarParser.CompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NegExpr.
    def visitNegExpr(self, ctx:GrammarParser.NegExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#OrExpr.
    def visitOrExpr(self, ctx:GrammarParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#CompareExp.
    def visitCompareExp(self, ctx:GrammarParser.CompareExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NegAExp.
    def visitNegAExp(self, ctx:GrammarParser.NegAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AndAExp.
    def visitAndAExp(self, ctx:GrammarParser.AndAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#OrAExp.
    def visitOrAExp(self, ctx:GrammarParser.OrAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BoolAExp.
    def visitBoolAExp(self, ctx:GrammarParser.BoolAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BAExp.
    def visitBAExp(self, ctx:GrammarParser.BAExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ProbCmd.
    def visitProbCmd(self, ctx:GrammarParser.ProbCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#WhileCmd.
    def visitWhileCmd(self, ctx:GrammarParser.WhileCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#UnifCmd.
    def visitUnifCmd(self, ctx:GrammarParser.UnifCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#SkipCmd.
    def visitSkipCmd(self, ctx:GrammarParser.SkipCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NonDetCmd.
    def visitNonDetCmd(self, ctx:GrammarParser.NonDetCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#IfElseCmd.
    def visitIfElseCmd(self, ctx:GrammarParser.IfElseCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AssCmd.
    def visitAssCmd(self, ctx:GrammarParser.AssCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#SeqCmd.
    def visitSeqCmd(self, ctx:GrammarParser.SeqCmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expectation.
    def visitExpectation(self, ctx:GrammarParser.ExpectationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ExprAExpPar.
    def visitExprAExpPar(self, ctx:GrammarParser.ExprAExpParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#IntAExpPar.
    def visitIntAExpPar(self, ctx:GrammarParser.IntAExpParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#RealAExpPar.
    def visitRealAExpPar(self, ctx:GrammarParser.RealAExpParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#VarAExpPar.
    def visitVarAExpPar(self, ctx:GrammarParser.VarAExpParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AExp.
    def visitAExp(self, ctx:GrammarParser.AExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#BExp.
    def visitBExp(self, ctx:GrammarParser.BExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#AddExp.
    def visitAddExp(self, ctx:GrammarParser.AddExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ScalExp.
    def visitScalExp(self, ctx:GrammarParser.ScalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Exp.
    def visitExp(self, ctx:GrammarParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#GuardExp.
    def visitGuardExp(self, ctx:GrammarParser.GuardExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Cons.
    def visitCons(self, ctx:GrammarParser.ConsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#Init.
    def visitInit(self, ctx:GrammarParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#InitSeq.
    def visitInitSeq(self, ctx:GrammarParser.InitSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#NoInit.
    def visitNoInit(self, ctx:GrammarParser.NoInitContext):
        return self.visitChildren(ctx)



del GrammarParser