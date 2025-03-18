# Generated from SnMsLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SnMsLangParser import SnMsLangParser
else:
    from SnMsLangParser import SnMsLangParser

# This class defines a complete listener for a parse tree produced by SnMsLangParser.
class SnMsLangListener(ParseTreeListener):

    # Enter a parse tree produced by SnMsLangParser#program.
    def enterProgram(self, ctx:SnMsLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#program.
    def exitProgram(self, ctx:SnMsLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#statement.
    def enterStatement(self, ctx:SnMsLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#statement.
    def exitStatement(self, ctx:SnMsLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#assignment.
    def enterAssignment(self, ctx:SnMsLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#assignment.
    def exitAssignment(self, ctx:SnMsLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#printStmt.
    def enterPrintStmt(self, ctx:SnMsLangParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#printStmt.
    def exitPrintStmt(self, ctx:SnMsLangParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#readStmt.
    def enterReadStmt(self, ctx:SnMsLangParser.ReadStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#readStmt.
    def exitReadStmt(self, ctx:SnMsLangParser.ReadStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#ifStmt.
    def enterIfStmt(self, ctx:SnMsLangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#ifStmt.
    def exitIfStmt(self, ctx:SnMsLangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#whileStmt.
    def enterWhileStmt(self, ctx:SnMsLangParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#whileStmt.
    def exitWhileStmt(self, ctx:SnMsLangParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#returnStmt.
    def enterReturnStmt(self, ctx:SnMsLangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#returnStmt.
    def exitReturnStmt(self, ctx:SnMsLangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#yieldStmt.
    def enterYieldStmt(self, ctx:SnMsLangParser.YieldStmtContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#yieldStmt.
    def exitYieldStmt(self, ctx:SnMsLangParser.YieldStmtContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#block.
    def enterBlock(self, ctx:SnMsLangParser.BlockContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#block.
    def exitBlock(self, ctx:SnMsLangParser.BlockContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#funcDecl.
    def enterFuncDecl(self, ctx:SnMsLangParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#funcDecl.
    def exitFuncDecl(self, ctx:SnMsLangParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#generatorDecl.
    def enterGeneratorDecl(self, ctx:SnMsLangParser.GeneratorDeclContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#generatorDecl.
    def exitGeneratorDecl(self, ctx:SnMsLangParser.GeneratorDeclContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#classDecl.
    def enterClassDecl(self, ctx:SnMsLangParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#classDecl.
    def exitClassDecl(self, ctx:SnMsLangParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#structDecl.
    def enterStructDecl(self, ctx:SnMsLangParser.StructDeclContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#structDecl.
    def exitStructDecl(self, ctx:SnMsLangParser.StructDeclContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#varDecl.
    def enterVarDecl(self, ctx:SnMsLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#varDecl.
    def exitVarDecl(self, ctx:SnMsLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#paramList.
    def enterParamList(self, ctx:SnMsLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#paramList.
    def exitParamList(self, ctx:SnMsLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#param.
    def enterParam(self, ctx:SnMsLangParser.ParamContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#param.
    def exitParam(self, ctx:SnMsLangParser.ParamContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#StringExpr.
    def enterStringExpr(self, ctx:SnMsLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#StringExpr.
    def exitStringExpr(self, ctx:SnMsLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#BoolExpr.
    def enterBoolExpr(self, ctx:SnMsLangParser.BoolExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#BoolExpr.
    def exitBoolExpr(self, ctx:SnMsLangParser.BoolExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#ArrayExpr.
    def enterArrayExpr(self, ctx:SnMsLangParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#ArrayExpr.
    def exitArrayExpr(self, ctx:SnMsLangParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#FloatExpr.
    def enterFloatExpr(self, ctx:SnMsLangParser.FloatExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#FloatExpr.
    def exitFloatExpr(self, ctx:SnMsLangParser.FloatExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:SnMsLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:SnMsLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#IdExpr.
    def enterIdExpr(self, ctx:SnMsLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#IdExpr.
    def exitIdExpr(self, ctx:SnMsLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#CompareExpr.
    def enterCompareExpr(self, ctx:SnMsLangParser.CompareExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#CompareExpr.
    def exitCompareExpr(self, ctx:SnMsLangParser.CompareExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#IntExpr.
    def enterIntExpr(self, ctx:SnMsLangParser.IntExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#IntExpr.
    def exitIntExpr(self, ctx:SnMsLangParser.IntExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#NotExpr.
    def enterNotExpr(self, ctx:SnMsLangParser.NotExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#NotExpr.
    def exitNotExpr(self, ctx:SnMsLangParser.NotExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#ParenExpr.
    def enterParenExpr(self, ctx:SnMsLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#ParenExpr.
    def exitParenExpr(self, ctx:SnMsLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:SnMsLangParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:SnMsLangParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#LogicalExpr.
    def enterLogicalExpr(self, ctx:SnMsLangParser.LogicalExprContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#LogicalExpr.
    def exitLogicalExpr(self, ctx:SnMsLangParser.LogicalExprContext):
        pass


    # Enter a parse tree produced by SnMsLangParser#typ.
    def enterTyp(self, ctx:SnMsLangParser.TypContext):
        pass

    # Exit a parse tree produced by SnMsLangParser#typ.
    def exitTyp(self, ctx:SnMsLangParser.TypContext):
        pass



del SnMsLangParser