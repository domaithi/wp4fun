# Generated from Grammar.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#PGCLProgram.
    def enterPGCLProgram(self, ctx:GrammarParser.PGCLProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#PGCLProgram.
    def exitPGCLProgram(self, ctx:GrammarParser.PGCLProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#PostExpectation.
    def enterPostExpectation(self, ctx:GrammarParser.PostExpectationContext):
        pass

    # Exit a parse tree produced by GrammarParser#PostExpectation.
    def exitPostExpectation(self, ctx:GrammarParser.PostExpectationContext):
        pass


    # Enter a parse tree produced by GrammarParser#PreExpectation.
    def enterPreExpectation(self, ctx:GrammarParser.PreExpectationContext):
        pass

    # Exit a parse tree produced by GrammarParser#PreExpectation.
    def exitPreExpectation(self, ctx:GrammarParser.PreExpectationContext):
        pass


    # Enter a parse tree produced by GrammarParser#Initializations.
    def enterInitializations(self, ctx:GrammarParser.InitializationsContext):
        pass

    # Exit a parse tree produced by GrammarParser#Initializations.
    def exitInitializations(self, ctx:GrammarParser.InitializationsContext):
        pass


    # Enter a parse tree produced by GrammarParser#MultDivExpr.
    def enterMultDivExpr(self, ctx:GrammarParser.MultDivExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#MultDivExpr.
    def exitMultDivExpr(self, ctx:GrammarParser.MultDivExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#PlusMinusDotminusExpr.
    def enterPlusMinusDotminusExpr(self, ctx:GrammarParser.PlusMinusDotminusExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#PlusMinusDotminusExpr.
    def exitPlusMinusDotminusExpr(self, ctx:GrammarParser.PlusMinusDotminusExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#Expr.
    def enterExpr(self, ctx:GrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#Expr.
    def exitExpr(self, ctx:GrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#VarExpr.
    def enterVarExpr(self, ctx:GrammarParser.VarExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#VarExpr.
    def exitVarExpr(self, ctx:GrammarParser.VarExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#IntExpr.
    def enterIntExpr(self, ctx:GrammarParser.IntExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#IntExpr.
    def exitIntExpr(self, ctx:GrammarParser.IntExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#VarAExp.
    def enterVarAExp(self, ctx:GrammarParser.VarAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#VarAExp.
    def exitVarAExp(self, ctx:GrammarParser.VarAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#ExprAExp.
    def enterExprAExp(self, ctx:GrammarParser.ExprAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#ExprAExp.
    def exitExprAExp(self, ctx:GrammarParser.ExprAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#PlusMinusDotminusAExp.
    def enterPlusMinusDotminusAExp(self, ctx:GrammarParser.PlusMinusDotminusAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#PlusMinusDotminusAExp.
    def exitPlusMinusDotminusAExp(self, ctx:GrammarParser.PlusMinusDotminusAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#IntAExp.
    def enterIntAExp(self, ctx:GrammarParser.IntAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#IntAExp.
    def exitIntAExp(self, ctx:GrammarParser.IntAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#RealAExp.
    def enterRealAExp(self, ctx:GrammarParser.RealAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#RealAExp.
    def exitRealAExp(self, ctx:GrammarParser.RealAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#MultDivAExp.
    def enterMultDivAExp(self, ctx:GrammarParser.MultDivAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#MultDivAExp.
    def exitMultDivAExp(self, ctx:GrammarParser.MultDivAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#AndExpr.
    def enterAndExpr(self, ctx:GrammarParser.AndExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#AndExpr.
    def exitAndExpr(self, ctx:GrammarParser.AndExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#BoolExpr.
    def enterBoolExpr(self, ctx:GrammarParser.BoolExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#BoolExpr.
    def exitBoolExpr(self, ctx:GrammarParser.BoolExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#BExpr.
    def enterBExpr(self, ctx:GrammarParser.BExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#BExpr.
    def exitBExpr(self, ctx:GrammarParser.BExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#CompareExpr.
    def enterCompareExpr(self, ctx:GrammarParser.CompareExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#CompareExpr.
    def exitCompareExpr(self, ctx:GrammarParser.CompareExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#NegExpr.
    def enterNegExpr(self, ctx:GrammarParser.NegExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#NegExpr.
    def exitNegExpr(self, ctx:GrammarParser.NegExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#OrExpr.
    def enterOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass

    # Exit a parse tree produced by GrammarParser#OrExpr.
    def exitOrExpr(self, ctx:GrammarParser.OrExprContext):
        pass


    # Enter a parse tree produced by GrammarParser#CompareExp.
    def enterCompareExp(self, ctx:GrammarParser.CompareExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#CompareExp.
    def exitCompareExp(self, ctx:GrammarParser.CompareExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#NegAExp.
    def enterNegAExp(self, ctx:GrammarParser.NegAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#NegAExp.
    def exitNegAExp(self, ctx:GrammarParser.NegAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#AndAExp.
    def enterAndAExp(self, ctx:GrammarParser.AndAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#AndAExp.
    def exitAndAExp(self, ctx:GrammarParser.AndAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#OrAExp.
    def enterOrAExp(self, ctx:GrammarParser.OrAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#OrAExp.
    def exitOrAExp(self, ctx:GrammarParser.OrAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#BoolAExp.
    def enterBoolAExp(self, ctx:GrammarParser.BoolAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#BoolAExp.
    def exitBoolAExp(self, ctx:GrammarParser.BoolAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#BAExp.
    def enterBAExp(self, ctx:GrammarParser.BAExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#BAExp.
    def exitBAExp(self, ctx:GrammarParser.BAExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#ProbCmd.
    def enterProbCmd(self, ctx:GrammarParser.ProbCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#ProbCmd.
    def exitProbCmd(self, ctx:GrammarParser.ProbCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#WhileCmd.
    def enterWhileCmd(self, ctx:GrammarParser.WhileCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#WhileCmd.
    def exitWhileCmd(self, ctx:GrammarParser.WhileCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#UnifCmd.
    def enterUnifCmd(self, ctx:GrammarParser.UnifCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#UnifCmd.
    def exitUnifCmd(self, ctx:GrammarParser.UnifCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#SkipCmd.
    def enterSkipCmd(self, ctx:GrammarParser.SkipCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#SkipCmd.
    def exitSkipCmd(self, ctx:GrammarParser.SkipCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#NonDetCmd.
    def enterNonDetCmd(self, ctx:GrammarParser.NonDetCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#NonDetCmd.
    def exitNonDetCmd(self, ctx:GrammarParser.NonDetCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#IfElseCmd.
    def enterIfElseCmd(self, ctx:GrammarParser.IfElseCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#IfElseCmd.
    def exitIfElseCmd(self, ctx:GrammarParser.IfElseCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#AssCmd.
    def enterAssCmd(self, ctx:GrammarParser.AssCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#AssCmd.
    def exitAssCmd(self, ctx:GrammarParser.AssCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#SeqCmd.
    def enterSeqCmd(self, ctx:GrammarParser.SeqCmdContext):
        pass

    # Exit a parse tree produced by GrammarParser#SeqCmd.
    def exitSeqCmd(self, ctx:GrammarParser.SeqCmdContext):
        pass


    # Enter a parse tree produced by GrammarParser#expectation.
    def enterExpectation(self, ctx:GrammarParser.ExpectationContext):
        pass

    # Exit a parse tree produced by GrammarParser#expectation.
    def exitExpectation(self, ctx:GrammarParser.ExpectationContext):
        pass


    # Enter a parse tree produced by GrammarParser#ExprAExpPar.
    def enterExprAExpPar(self, ctx:GrammarParser.ExprAExpParContext):
        pass

    # Exit a parse tree produced by GrammarParser#ExprAExpPar.
    def exitExprAExpPar(self, ctx:GrammarParser.ExprAExpParContext):
        pass


    # Enter a parse tree produced by GrammarParser#IntAExpPar.
    def enterIntAExpPar(self, ctx:GrammarParser.IntAExpParContext):
        pass

    # Exit a parse tree produced by GrammarParser#IntAExpPar.
    def exitIntAExpPar(self, ctx:GrammarParser.IntAExpParContext):
        pass


    # Enter a parse tree produced by GrammarParser#RealAExpPar.
    def enterRealAExpPar(self, ctx:GrammarParser.RealAExpParContext):
        pass

    # Exit a parse tree produced by GrammarParser#RealAExpPar.
    def exitRealAExpPar(self, ctx:GrammarParser.RealAExpParContext):
        pass


    # Enter a parse tree produced by GrammarParser#VarAExpPar.
    def enterVarAExpPar(self, ctx:GrammarParser.VarAExpParContext):
        pass

    # Exit a parse tree produced by GrammarParser#VarAExpPar.
    def exitVarAExpPar(self, ctx:GrammarParser.VarAExpParContext):
        pass


    # Enter a parse tree produced by GrammarParser#AExp.
    def enterAExp(self, ctx:GrammarParser.AExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#AExp.
    def exitAExp(self, ctx:GrammarParser.AExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#BExp.
    def enterBExp(self, ctx:GrammarParser.BExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#BExp.
    def exitBExp(self, ctx:GrammarParser.BExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#AddExp.
    def enterAddExp(self, ctx:GrammarParser.AddExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#AddExp.
    def exitAddExp(self, ctx:GrammarParser.AddExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#ScalExp.
    def enterScalExp(self, ctx:GrammarParser.ScalExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#ScalExp.
    def exitScalExp(self, ctx:GrammarParser.ScalExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#Exp.
    def enterExp(self, ctx:GrammarParser.ExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#Exp.
    def exitExp(self, ctx:GrammarParser.ExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#GuardExp.
    def enterGuardExp(self, ctx:GrammarParser.GuardExpContext):
        pass

    # Exit a parse tree produced by GrammarParser#GuardExp.
    def exitGuardExp(self, ctx:GrammarParser.GuardExpContext):
        pass


    # Enter a parse tree produced by GrammarParser#Cons.
    def enterCons(self, ctx:GrammarParser.ConsContext):
        pass

    # Exit a parse tree produced by GrammarParser#Cons.
    def exitCons(self, ctx:GrammarParser.ConsContext):
        pass


    # Enter a parse tree produced by GrammarParser#Init.
    def enterInit(self, ctx:GrammarParser.InitContext):
        pass

    # Exit a parse tree produced by GrammarParser#Init.
    def exitInit(self, ctx:GrammarParser.InitContext):
        pass


    # Enter a parse tree produced by GrammarParser#InitSeq.
    def enterInitSeq(self, ctx:GrammarParser.InitSeqContext):
        pass

    # Exit a parse tree produced by GrammarParser#InitSeq.
    def exitInitSeq(self, ctx:GrammarParser.InitSeqContext):
        pass


    # Enter a parse tree produced by GrammarParser#NoInit.
    def enterNoInit(self, ctx:GrammarParser.NoInitContext):
        pass

    # Exit a parse tree produced by GrammarParser#NoInit.
    def exitNoInit(self, ctx:GrammarParser.NoInitContext):
        pass



del GrammarParser