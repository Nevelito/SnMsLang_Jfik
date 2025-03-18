# Generated from SnMsLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,237,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,4,0,40,8,0,
        11,0,12,0,41,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        56,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,82,8,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,5,9,100,8,9,10,9,
        12,9,103,9,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,111,8,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,3,11,120,8,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,5,12,130,8,12,10,12,12,12,133,9,12,1,12,1,12,1,13,
        1,13,1,13,1,13,5,13,141,8,13,10,13,12,13,144,9,13,1,13,1,13,1,14,
        3,14,149,8,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,157,8,14,10,14,
        12,14,160,9,14,1,14,5,14,163,8,14,10,14,12,14,166,9,14,1,14,1,14,
        1,15,1,15,1,15,5,15,173,8,15,10,15,12,15,176,9,15,1,16,3,16,179,
        8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,189,8,17,10,17,
        12,17,192,9,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,3,17,207,8,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,5,17,221,8,17,10,17,12,17,224,9,17,1,18,
        1,18,1,18,3,18,229,8,18,1,18,1,18,1,18,1,18,3,18,235,8,18,1,18,0,
        1,34,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,6,
        1,0,18,19,1,0,23,24,1,0,25,26,1,0,27,31,1,0,32,34,1,0,38,39,259,
        0,39,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,62,1,0,0,0,8,68,1,0,0,0,
        10,74,1,0,0,0,12,83,1,0,0,0,14,89,1,0,0,0,16,93,1,0,0,0,18,97,1,
        0,0,0,20,106,1,0,0,0,22,115,1,0,0,0,24,124,1,0,0,0,26,136,1,0,0,
        0,28,148,1,0,0,0,30,169,1,0,0,0,32,178,1,0,0,0,34,206,1,0,0,0,36,
        234,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,
        0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,56,3,4,2,0,44,56,3,6,3,0,45,56,
        3,8,4,0,46,56,3,10,5,0,47,56,3,12,6,0,48,56,3,20,10,0,49,56,3,22,
        11,0,50,56,3,28,14,0,51,56,3,24,12,0,52,56,3,26,13,0,53,56,3,14,
        7,0,54,56,3,16,8,0,55,43,1,0,0,0,55,44,1,0,0,0,55,45,1,0,0,0,55,
        46,1,0,0,0,55,47,1,0,0,0,55,48,1,0,0,0,55,49,1,0,0,0,55,50,1,0,0,
        0,55,51,1,0,0,0,55,52,1,0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,3,1,
        0,0,0,57,58,5,44,0,0,58,59,5,1,0,0,59,60,3,34,17,0,60,61,5,2,0,0,
        61,5,1,0,0,0,62,63,5,3,0,0,63,64,5,4,0,0,64,65,3,34,17,0,65,66,5,
        5,0,0,66,67,5,2,0,0,67,7,1,0,0,0,68,69,5,6,0,0,69,70,5,4,0,0,70,
        71,5,44,0,0,71,72,5,5,0,0,72,73,5,2,0,0,73,9,1,0,0,0,74,75,5,7,0,
        0,75,76,5,4,0,0,76,77,3,34,17,0,77,78,5,5,0,0,78,81,3,18,9,0,79,
        80,5,8,0,0,80,82,3,18,9,0,81,79,1,0,0,0,81,82,1,0,0,0,82,11,1,0,
        0,0,83,84,5,9,0,0,84,85,5,4,0,0,85,86,3,34,17,0,86,87,5,5,0,0,87,
        88,3,18,9,0,88,13,1,0,0,0,89,90,5,10,0,0,90,91,3,34,17,0,91,92,5,
        2,0,0,92,15,1,0,0,0,93,94,5,11,0,0,94,95,3,34,17,0,95,96,5,2,0,0,
        96,17,1,0,0,0,97,101,5,12,0,0,98,100,3,2,1,0,99,98,1,0,0,0,100,103,
        1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,
        0,0,0,104,105,5,13,0,0,105,19,1,0,0,0,106,107,5,14,0,0,107,108,5,
        44,0,0,108,110,5,4,0,0,109,111,3,30,15,0,110,109,1,0,0,0,110,111,
        1,0,0,0,111,112,1,0,0,0,112,113,5,5,0,0,113,114,3,18,9,0,114,21,
        1,0,0,0,115,116,5,15,0,0,116,117,5,44,0,0,117,119,5,4,0,0,118,120,
        3,30,15,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,1,0,0,0,121,122,
        5,5,0,0,122,123,3,18,9,0,123,23,1,0,0,0,124,125,5,16,0,0,125,126,
        5,44,0,0,126,131,5,12,0,0,127,130,3,28,14,0,128,130,3,20,10,0,129,
        127,1,0,0,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,
        132,1,0,0,0,132,134,1,0,0,0,133,131,1,0,0,0,134,135,5,13,0,0,135,
        25,1,0,0,0,136,137,5,17,0,0,137,138,5,44,0,0,138,142,5,12,0,0,139,
        141,3,28,14,0,140,139,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,
        143,1,0,0,0,143,145,1,0,0,0,144,142,1,0,0,0,145,146,5,13,0,0,146,
        27,1,0,0,0,147,149,7,0,0,0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,
        1,0,0,0,150,151,3,36,18,0,151,164,5,44,0,0,152,153,5,20,0,0,153,
        158,5,45,0,0,154,155,5,21,0,0,155,157,5,45,0,0,156,154,1,0,0,0,157,
        160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,
        158,1,0,0,0,161,163,5,22,0,0,162,152,1,0,0,0,163,166,1,0,0,0,164,
        162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,
        168,5,2,0,0,168,29,1,0,0,0,169,174,3,32,16,0,170,171,5,21,0,0,171,
        173,3,32,16,0,172,170,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,31,1,0,0,0,176,174,1,0,0,0,177,179,3,36,18,0,178,
        177,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,181,5,44,0,0,181,
        33,1,0,0,0,182,183,6,17,-1,0,183,184,5,44,0,0,184,185,5,20,0,0,185,
        190,3,34,17,0,186,187,5,21,0,0,187,189,3,34,17,0,188,186,1,0,0,0,
        189,192,1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,193,1,0,0,0,
        192,190,1,0,0,0,193,194,5,22,0,0,194,207,1,0,0,0,195,207,5,44,0,
        0,196,207,5,45,0,0,197,207,5,46,0,0,198,207,5,47,0,0,199,207,5,48,
        0,0,200,201,5,4,0,0,201,202,3,34,17,0,202,203,5,5,0,0,203,207,1,
        0,0,0,204,205,5,35,0,0,205,207,3,34,17,1,206,182,1,0,0,0,206,195,
        1,0,0,0,206,196,1,0,0,0,206,197,1,0,0,0,206,198,1,0,0,0,206,199,
        1,0,0,0,206,200,1,0,0,0,206,204,1,0,0,0,207,222,1,0,0,0,208,209,
        10,12,0,0,209,210,7,1,0,0,210,221,3,34,17,13,211,212,10,11,0,0,212,
        213,7,2,0,0,213,221,3,34,17,12,214,215,10,10,0,0,215,216,7,3,0,0,
        216,221,3,34,17,11,217,218,10,9,0,0,218,219,7,4,0,0,219,221,3,34,
        17,10,220,208,1,0,0,0,220,211,1,0,0,0,220,214,1,0,0,0,220,217,1,
        0,0,0,221,224,1,0,0,0,222,220,1,0,0,0,222,223,1,0,0,0,223,35,1,0,
        0,0,224,222,1,0,0,0,225,235,5,36,0,0,226,228,5,37,0,0,227,229,7,
        5,0,0,228,227,1,0,0,0,228,229,1,0,0,0,229,235,1,0,0,0,230,235,5,
        40,0,0,231,235,5,41,0,0,232,235,5,42,0,0,233,235,5,43,0,0,234,225,
        1,0,0,0,234,226,1,0,0,0,234,230,1,0,0,0,234,231,1,0,0,0,234,232,
        1,0,0,0,234,233,1,0,0,0,235,37,1,0,0,0,20,41,55,81,101,110,119,129,
        131,142,148,158,164,174,178,190,206,220,222,228,234
    ]

class SnMsLangParser ( Parser ):

    grammarFileName = "SnMsLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'wypisz'", "'('", "')'", 
                     "'wczytaj'", "'jezeli'", "'inaczej'", "'dopoki'", "'zwroc'", 
                     "'yield'", "'{'", "'}'", "'funkcja'", "'generator'", 
                     "'klasa'", "'struktura'", "'globalna'", "'lokalna'", 
                     "'['", "','", "']'", "'*'", "'/'", "'+'", "'-'", "'=='", 
                     "'!='", "'<'", "'>'", "'<>'", "'&&'", "'||'", "'^'", 
                     "'!'", "'liczba'", "'zmiennoprzecinkowa'", "'32'", 
                     "'64'", "'tekst'", "'bool'", "'zmienna'", "'dynamiczny'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "STRING", "BOOL", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_printStmt = 3
    RULE_readStmt = 4
    RULE_ifStmt = 5
    RULE_whileStmt = 6
    RULE_returnStmt = 7
    RULE_yieldStmt = 8
    RULE_block = 9
    RULE_funcDecl = 10
    RULE_generatorDecl = 11
    RULE_classDecl = 12
    RULE_structDecl = 13
    RULE_varDecl = 14
    RULE_paramList = 15
    RULE_param = 16
    RULE_expr = 17
    RULE_typ = 18

    ruleNames =  [ "program", "statement", "assignment", "printStmt", "readStmt", 
                   "ifStmt", "whileStmt", "returnStmt", "yieldStmt", "block", 
                   "funcDecl", "generatorDecl", "classDecl", "structDecl", 
                   "varDecl", "paramList", "param", "expr", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    ID=44
    INT=45
    FLOAT=46
    STRING=47
    BOOL=48
    WS=49
    ERROR_CHAR=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = SnMsLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self.statement()
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34291019927240) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(SnMsLangParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.PrintStmtContext,0)


        def readStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.ReadStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.WhileStmtContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(SnMsLangParser.FuncDeclContext,0)


        def generatorDecl(self):
            return self.getTypedRuleContext(SnMsLangParser.GeneratorDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(SnMsLangParser.VarDeclContext,0)


        def classDecl(self):
            return self.getTypedRuleContext(SnMsLangParser.ClassDeclContext,0)


        def structDecl(self):
            return self.getTypedRuleContext(SnMsLangParser.StructDeclContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.ReturnStmtContext,0)


        def yieldStmt(self):
            return self.getTypedRuleContext(SnMsLangParser.YieldStmtContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SnMsLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.printStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.readStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.ifStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.whileStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.funcDecl()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.generatorDecl()
                pass
            elif token in [18, 19, 36, 37, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.varDecl()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.classDecl()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 10)
                self.state = 52
                self.structDecl()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 11)
                self.state = 53
                self.returnStmt()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 12)
                self.state = 54
                self.yieldStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = SnMsLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SnMsLangParser.ID)
            self.state = 58
            self.match(SnMsLangParser.T__0)
            self.state = 59
            self.expr(0)
            self.state = 60
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = SnMsLangParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SnMsLangParser.T__2)
            self.state = 63
            self.match(SnMsLangParser.T__3)
            self.state = 64
            self.expr(0)
            self.state = 65
            self.match(SnMsLangParser.T__4)
            self.state = 66
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def getRuleIndex(self):
            return SnMsLangParser.RULE_readStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStmt" ):
                listener.enterReadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStmt" ):
                listener.exitReadStmt(self)




    def readStmt(self):

        localctx = SnMsLangParser.ReadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_readStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(SnMsLangParser.T__5)
            self.state = 69
            self.match(SnMsLangParser.T__3)
            self.state = 70
            self.match(SnMsLangParser.ID)
            self.state = 71
            self.match(SnMsLangParser.T__4)
            self.state = 72
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.BlockContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = SnMsLangParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(SnMsLangParser.T__6)
            self.state = 75
            self.match(SnMsLangParser.T__3)
            self.state = 76
            self.expr(0)
            self.state = 77
            self.match(SnMsLangParser.T__4)
            self.state = 78
            self.block()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 79
                self.match(SnMsLangParser.T__7)
                self.state = 80
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(SnMsLangParser.BlockContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = SnMsLangParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(SnMsLangParser.T__8)
            self.state = 84
            self.match(SnMsLangParser.T__3)
            self.state = 85
            self.expr(0)
            self.state = 86
            self.match(SnMsLangParser.T__4)
            self.state = 87
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = SnMsLangParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(SnMsLangParser.T__9)
            self.state = 90
            self.expr(0)
            self.state = 91
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YieldStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_yieldStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterYieldStmt" ):
                listener.enterYieldStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitYieldStmt" ):
                listener.exitYieldStmt(self)




    def yieldStmt(self):

        localctx = SnMsLangParser.YieldStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_yieldStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(SnMsLangParser.T__10)
            self.state = 94
            self.expr(0)
            self.state = 95
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = SnMsLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(SnMsLangParser.T__11)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34291019927240) != 0):
                self.state = 98
                self.statement()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(SnMsLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(SnMsLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(SnMsLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)




    def funcDecl(self):

        localctx = SnMsLangParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SnMsLangParser.T__13)
            self.state = 107
            self.match(SnMsLangParser.ID)
            self.state = 108
            self.match(SnMsLangParser.T__3)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34291018891264) != 0):
                self.state = 109
                self.paramList()


            self.state = 112
            self.match(SnMsLangParser.T__4)
            self.state = 113
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeneratorDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(SnMsLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(SnMsLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_generatorDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneratorDecl" ):
                listener.enterGeneratorDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneratorDecl" ):
                listener.exitGeneratorDecl(self)




    def generatorDecl(self):

        localctx = SnMsLangParser.GeneratorDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_generatorDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(SnMsLangParser.T__14)
            self.state = 116
            self.match(SnMsLangParser.ID)
            self.state = 117
            self.match(SnMsLangParser.T__3)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34291018891264) != 0):
                self.state = 118
                self.paramList()


            self.state = 121
            self.match(SnMsLangParser.T__4)
            self.state = 122
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.VarDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)




    def classDecl(self):

        localctx = SnMsLangParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(SnMsLangParser.T__15)
            self.state = 125
            self.match(SnMsLangParser.ID)
            self.state = 126
            self.match(SnMsLangParser.T__11)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16698833649664) != 0):
                self.state = 129
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [18, 19, 36, 37, 40, 41, 42, 43]:
                    self.state = 127
                    self.varDecl()
                    pass
                elif token in [14]:
                    self.state = 128
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
            self.match(SnMsLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.VarDeclContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_structDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDecl" ):
                listener.enterStructDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDecl" ):
                listener.exitStructDecl(self)




    def structDecl(self):

        localctx = SnMsLangParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(SnMsLangParser.T__16)
            self.state = 137
            self.match(SnMsLangParser.ID)
            self.state = 138
            self.match(SnMsLangParser.T__11)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 16698833633280) != 0):
                self.state = 139
                self.varDecl()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 145
            self.match(SnMsLangParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(SnMsLangParser.TypContext,0)


        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SnMsLangParser.INT)
            else:
                return self.getToken(SnMsLangParser.INT, i)

        def getRuleIndex(self):
            return SnMsLangParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = SnMsLangParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18 or _la==19:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 150
            self.typ()
            self.state = 151
            self.match(SnMsLangParser.ID)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 152
                self.match(SnMsLangParser.T__19)
                self.state = 153
                self.match(SnMsLangParser.INT)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 154
                    self.match(SnMsLangParser.T__20)
                    self.state = 155
                    self.match(SnMsLangParser.INT)
                    self.state = 160
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 161
                self.match(SnMsLangParser.T__21)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(SnMsLangParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ParamContext,i)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = SnMsLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.param()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 170
                self.match(SnMsLangParser.T__20)
                self.state = 171
                self.param()
                self.state = 176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(SnMsLangParser.TypContext,0)


        def getRuleIndex(self):
            return SnMsLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = SnMsLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 16698832846848) != 0):
                self.state = 177
                self.typ()


            self.state = 180
            self.match(SnMsLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SnMsLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(SnMsLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)


    class BoolExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(SnMsLangParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)


    class ArrayExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)


    class FloatExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SnMsLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)


    class MulDivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SnMsLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class CompareExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)


    class IntExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SnMsLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntExpr" ):
                listener.enterIntExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntExpr" ):
                listener.exitIntExpr(self)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SnMsLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class AddSubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)


    class LogicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SnMsLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SnMsLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(SnMsLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SnMsLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                localctx = SnMsLangParser.ArrayExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 183
                self.match(SnMsLangParser.ID)
                self.state = 184
                self.match(SnMsLangParser.T__19)
                self.state = 185
                self.expr(0)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 186
                    self.match(SnMsLangParser.T__20)
                    self.state = 187
                    self.expr(0)
                    self.state = 192
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 193
                self.match(SnMsLangParser.T__21)
                pass

            elif la_ == 2:
                localctx = SnMsLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                self.match(SnMsLangParser.ID)
                pass

            elif la_ == 3:
                localctx = SnMsLangParser.IntExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                self.match(SnMsLangParser.INT)
                pass

            elif la_ == 4:
                localctx = SnMsLangParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                self.match(SnMsLangParser.FLOAT)
                pass

            elif la_ == 5:
                localctx = SnMsLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(SnMsLangParser.STRING)
                pass

            elif la_ == 6:
                localctx = SnMsLangParser.BoolExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(SnMsLangParser.BOOL)
                pass

            elif la_ == 7:
                localctx = SnMsLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 200
                self.match(SnMsLangParser.T__3)
                self.state = 201
                self.expr(0)
                self.state = 202
                self.match(SnMsLangParser.T__4)
                pass

            elif la_ == 8:
                localctx = SnMsLangParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 204
                self.match(SnMsLangParser.T__34)
                self.state = 205
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 222
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 220
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = SnMsLangParser.MulDivExprContext(self, SnMsLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 209
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 210
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = SnMsLangParser.AddSubExprContext(self, SnMsLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 211
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 212
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 213
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = SnMsLangParser.CompareExprContext(self, SnMsLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 215
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 216
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = SnMsLangParser.LogicalExprContext(self, SnMsLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 218
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 219
                        self.expr(10)
                        pass

             
                self.state = 224
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SnMsLangParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = SnMsLangParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(SnMsLangParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(SnMsLangParser.T__36)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38 or _la==39:
                    self.state = 227
                    _la = self._input.LA(1)
                    if not(_la==38 or _la==39):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(SnMsLangParser.T__39)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.match(SnMsLangParser.T__40)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.match(SnMsLangParser.T__41)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 6)
                self.state = 233
                self.match(SnMsLangParser.T__42)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[17] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         




