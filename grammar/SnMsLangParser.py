# Generated from grammar/SnMsLang.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\64")
        buf.write("\u00ef\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\6\2*\n\2\r\2\16\2+\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7T\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\7\13")
        buf.write("f\n\13\f\13\16\13i\13\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f")
        buf.write("q\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\rz\n\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\7\16\u0084\n\16\f\16\16\16\u0087")
        buf.write("\13\16\3\16\3\16\3\17\3\17\3\17\3\17\7\17\u008f\n\17\f")
        buf.write("\17\16\17\u0092\13\17\3\17\3\17\3\20\5\20\u0097\n\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\7\20\u009f\n\20\f\20\16\20")
        buf.write("\u00a2\13\20\3\20\7\20\u00a5\n\20\f\20\16\20\u00a8\13")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\7\21\u00af\n\21\f\21\16\21")
        buf.write("\u00b2\13\21\3\22\5\22\u00b5\n\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00bf\n\23\f\23\16\23\u00c2")
        buf.write("\13\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u00d1\n\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00df\n")
        buf.write("\23\f\23\16\23\u00e2\13\23\3\24\3\24\3\24\5\24\u00e7\n")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u00ed\n\24\3\24\2\3$\25\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\b\3\2\24")
        buf.write("\25\3\2\31\32\3\2\33\34\3\2\35!\3\2\"$\3\2()\2\u0105\2")
        buf.write(")\3\2\2\2\49\3\2\2\2\6;\3\2\2\2\b@\3\2\2\2\nF\3\2\2\2")
        buf.write("\fL\3\2\2\2\16U\3\2\2\2\20[\3\2\2\2\22_\3\2\2\2\24c\3")
        buf.write("\2\2\2\26l\3\2\2\2\30u\3\2\2\2\32~\3\2\2\2\34\u008a\3")
        buf.write("\2\2\2\36\u0096\3\2\2\2 \u00ab\3\2\2\2\"\u00b4\3\2\2\2")
        buf.write("$\u00d0\3\2\2\2&\u00ec\3\2\2\2(*\5\4\3\2)(\3\2\2\2*+\3")
        buf.write("\2\2\2+)\3\2\2\2+,\3\2\2\2,\3\3\2\2\2-:\5\6\4\2.:\5\b")
        buf.write("\5\2/:\5\n\6\2\60:\5\f\7\2\61:\5\16\b\2\62:\5\26\f\2\63")
        buf.write(":\5\30\r\2\64:\5\36\20\2\65:\5\32\16\2\66:\5\34\17\2\67")
        buf.write(":\5\20\t\28:\5\22\n\29-\3\2\2\29.\3\2\2\29/\3\2\2\29\60")
        buf.write("\3\2\2\29\61\3\2\2\29\62\3\2\2\29\63\3\2\2\29\64\3\2\2")
        buf.write("\29\65\3\2\2\29\66\3\2\2\29\67\3\2\2\298\3\2\2\2:\5\3")
        buf.write("\2\2\2;<\7.\2\2<=\7\3\2\2=>\5$\23\2>?\7\4\2\2?\7\3\2\2")
        buf.write("\2@A\7\5\2\2AB\7\6\2\2BC\5$\23\2CD\7\7\2\2DE\7\4\2\2E")
        buf.write("\t\3\2\2\2FG\7\b\2\2GH\7\6\2\2HI\7.\2\2IJ\7\7\2\2JK\7")
        buf.write("\4\2\2K\13\3\2\2\2LM\7\t\2\2MN\7\6\2\2NO\5$\23\2OP\7\7")
        buf.write("\2\2PS\5\24\13\2QR\7\n\2\2RT\5\24\13\2SQ\3\2\2\2ST\3\2")
        buf.write("\2\2T\r\3\2\2\2UV\7\13\2\2VW\7\6\2\2WX\5$\23\2XY\7\7\2")
        buf.write("\2YZ\5\24\13\2Z\17\3\2\2\2[\\\7\f\2\2\\]\5$\23\2]^\7\4")
        buf.write("\2\2^\21\3\2\2\2_`\7\r\2\2`a\5$\23\2ab\7\4\2\2b\23\3\2")
        buf.write("\2\2cg\7\16\2\2df\5\4\3\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2")
        buf.write("\2gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2jk\7\17\2\2k\25\3\2\2")
        buf.write("\2lm\7\20\2\2mn\7.\2\2np\7\6\2\2oq\5 \21\2po\3\2\2\2p")
        buf.write("q\3\2\2\2qr\3\2\2\2rs\7\7\2\2st\5\24\13\2t\27\3\2\2\2")
        buf.write("uv\7\21\2\2vw\7.\2\2wy\7\6\2\2xz\5 \21\2yx\3\2\2\2yz\3")
        buf.write("\2\2\2z{\3\2\2\2{|\7\7\2\2|}\5\24\13\2}\31\3\2\2\2~\177")
        buf.write("\7\22\2\2\177\u0080\7.\2\2\u0080\u0085\7\16\2\2\u0081")
        buf.write("\u0084\5\36\20\2\u0082\u0084\5\26\f\2\u0083\u0081\3\2")
        buf.write("\2\2\u0083\u0082\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u0089\7\17\2\2\u0089\33\3\2\2\2\u008a")
        buf.write("\u008b\7\23\2\2\u008b\u008c\7.\2\2\u008c\u0090\7\16\2")
        buf.write("\2\u008d\u008f\5\36\20\2\u008e\u008d\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\u0093\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\7\17\2")
        buf.write("\2\u0094\35\3\2\2\2\u0095\u0097\t\2\2\2\u0096\u0095\3")
        buf.write("\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0099")
        buf.write("\5&\24\2\u0099\u00a6\7.\2\2\u009a\u009b\7\26\2\2\u009b")
        buf.write("\u00a0\7/\2\2\u009c\u009d\7\27\2\2\u009d\u009f\7/\2\2")
        buf.write("\u009e\u009c\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3")
        buf.write("\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a5\7\30\2\2\u00a4\u009a\3\2\2\2\u00a5")
        buf.write("\u00a8\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2")
        buf.write("\u00a7\u00a9\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\7")
        buf.write("\4\2\2\u00aa\37\3\2\2\2\u00ab\u00b0\5\"\22\2\u00ac\u00ad")
        buf.write("\7\27\2\2\u00ad\u00af\5\"\22\2\u00ae\u00ac\3\2\2\2\u00af")
        buf.write("\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2")
        buf.write("\u00b1!\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b3\u00b5\5&\24")
        buf.write("\2\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\u00b7\7.\2\2\u00b7#\3\2\2\2\u00b8\u00b9")
        buf.write("\b\23\1\2\u00b9\u00ba\7.\2\2\u00ba\u00bb\7\26\2\2\u00bb")
        buf.write("\u00c0\5$\23\2\u00bc\u00bd\7\27\2\2\u00bd\u00bf\5$\23")
        buf.write("\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0\u00be")
        buf.write("\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c4\7\30\2\2\u00c4\u00d1\3\2\2")
        buf.write("\2\u00c5\u00d1\7.\2\2\u00c6\u00d1\7/\2\2\u00c7\u00d1\7")
        buf.write("\60\2\2\u00c8\u00d1\7\61\2\2\u00c9\u00d1\7\62\2\2\u00ca")
        buf.write("\u00cb\7\6\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd\7\7\2\2")
        buf.write("\u00cd\u00d1\3\2\2\2\u00ce\u00cf\7%\2\2\u00cf\u00d1\5")
        buf.write("$\23\3\u00d0\u00b8\3\2\2\2\u00d0\u00c5\3\2\2\2\u00d0\u00c6")
        buf.write("\3\2\2\2\u00d0\u00c7\3\2\2\2\u00d0\u00c8\3\2\2\2\u00d0")
        buf.write("\u00c9\3\2\2\2\u00d0\u00ca\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d1\u00e0\3\2\2\2\u00d2\u00d3\f\16\2\2\u00d3\u00d4")
        buf.write("\t\3\2\2\u00d4\u00df\5$\23\17\u00d5\u00d6\f\r\2\2\u00d6")
        buf.write("\u00d7\t\4\2\2\u00d7\u00df\5$\23\16\u00d8\u00d9\f\f\2")
        buf.write("\2\u00d9\u00da\t\5\2\2\u00da\u00df\5$\23\r\u00db\u00dc")
        buf.write("\f\13\2\2\u00dc\u00dd\t\6\2\2\u00dd\u00df\5$\23\f\u00de")
        buf.write("\u00d2\3\2\2\2\u00de\u00d5\3\2\2\2\u00de\u00d8\3\2\2\2")
        buf.write("\u00de\u00db\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1%\3\2\2\2\u00e2\u00e0")
        buf.write("\3\2\2\2\u00e3\u00ed\7&\2\2\u00e4\u00e6\7\'\2\2\u00e5")
        buf.write("\u00e7\t\7\2\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00ed\3\2\2\2\u00e8\u00ed\7*\2\2\u00e9\u00ed\7")
        buf.write("+\2\2\u00ea\u00ed\7,\2\2\u00eb\u00ed\7-\2\2\u00ec\u00e3")
        buf.write("\3\2\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec")
        buf.write("\u00e9\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\'\3\2\2\2\26+9Sgpy\u0083\u0085\u0090\u0096\u00a0")
        buf.write("\u00a6\u00b0\u00b4\u00c0\u00d0\u00de\u00e0\u00e6\u00ec")
        return buf.getvalue()


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
        self.checkVersion("4.9.3")
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__2) | (1 << SnMsLangParser.T__5) | (1 << SnMsLangParser.T__6) | (1 << SnMsLangParser.T__8) | (1 << SnMsLangParser.T__9) | (1 << SnMsLangParser.T__10) | (1 << SnMsLangParser.T__13) | (1 << SnMsLangParser.T__14) | (1 << SnMsLangParser.T__15) | (1 << SnMsLangParser.T__16) | (1 << SnMsLangParser.T__17) | (1 << SnMsLangParser.T__18) | (1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42) | (1 << SnMsLangParser.ID))) != 0)):
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
            if token in [SnMsLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.assignment()
                pass
            elif token in [SnMsLangParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.printStmt()
                pass
            elif token in [SnMsLangParser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.readStmt()
                pass
            elif token in [SnMsLangParser.T__6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.ifStmt()
                pass
            elif token in [SnMsLangParser.T__8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.whileStmt()
                pass
            elif token in [SnMsLangParser.T__13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.funcDecl()
                pass
            elif token in [SnMsLangParser.T__14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.generatorDecl()
                pass
            elif token in [SnMsLangParser.T__17, SnMsLangParser.T__18, SnMsLangParser.T__35, SnMsLangParser.T__36, SnMsLangParser.T__39, SnMsLangParser.T__40, SnMsLangParser.T__41, SnMsLangParser.T__42]:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.varDecl()
                pass
            elif token in [SnMsLangParser.T__15]:
                self.enterOuterAlt(localctx, 9)
                self.state = 51
                self.classDecl()
                pass
            elif token in [SnMsLangParser.T__16]:
                self.enterOuterAlt(localctx, 10)
                self.state = 52
                self.structDecl()
                pass
            elif token in [SnMsLangParser.T__9]:
                self.enterOuterAlt(localctx, 11)
                self.state = 53
                self.returnStmt()
                pass
            elif token in [SnMsLangParser.T__10]:
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
            if _la==SnMsLangParser.T__7:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__2) | (1 << SnMsLangParser.T__5) | (1 << SnMsLangParser.T__6) | (1 << SnMsLangParser.T__8) | (1 << SnMsLangParser.T__9) | (1 << SnMsLangParser.T__10) | (1 << SnMsLangParser.T__13) | (1 << SnMsLangParser.T__14) | (1 << SnMsLangParser.T__15) | (1 << SnMsLangParser.T__16) | (1 << SnMsLangParser.T__17) | (1 << SnMsLangParser.T__18) | (1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42) | (1 << SnMsLangParser.ID))) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42) | (1 << SnMsLangParser.ID))) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42) | (1 << SnMsLangParser.ID))) != 0):
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__13) | (1 << SnMsLangParser.T__17) | (1 << SnMsLangParser.T__18) | (1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42))) != 0):
                self.state = 129
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SnMsLangParser.T__17, SnMsLangParser.T__18, SnMsLangParser.T__35, SnMsLangParser.T__36, SnMsLangParser.T__39, SnMsLangParser.T__40, SnMsLangParser.T__41, SnMsLangParser.T__42]:
                    self.state = 127
                    self.varDecl()
                    pass
                elif token in [SnMsLangParser.T__13]:
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__17) | (1 << SnMsLangParser.T__18) | (1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42))) != 0):
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
            if _la==SnMsLangParser.T__17 or _la==SnMsLangParser.T__18:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==SnMsLangParser.T__17 or _la==SnMsLangParser.T__18):
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
            while _la==SnMsLangParser.T__19:
                self.state = 152
                self.match(SnMsLangParser.T__19)
                self.state = 153
                self.match(SnMsLangParser.INT)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==SnMsLangParser.T__20:
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
            while _la==SnMsLangParser.T__20:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__35) | (1 << SnMsLangParser.T__36) | (1 << SnMsLangParser.T__39) | (1 << SnMsLangParser.T__40) | (1 << SnMsLangParser.T__41) | (1 << SnMsLangParser.T__42))) != 0):
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
                while _la==SnMsLangParser.T__20:
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
                        if not(_la==SnMsLangParser.T__22 or _la==SnMsLangParser.T__23):
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
                        if not(_la==SnMsLangParser.T__24 or _la==SnMsLangParser.T__25):
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__26) | (1 << SnMsLangParser.T__27) | (1 << SnMsLangParser.T__28) | (1 << SnMsLangParser.T__29) | (1 << SnMsLangParser.T__30))) != 0)):
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
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SnMsLangParser.T__31) | (1 << SnMsLangParser.T__32) | (1 << SnMsLangParser.T__33))) != 0)):
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
            if token in [SnMsLangParser.T__35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.match(SnMsLangParser.T__35)
                pass
            elif token in [SnMsLangParser.T__36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(SnMsLangParser.T__36)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SnMsLangParser.T__37 or _la==SnMsLangParser.T__38:
                    self.state = 227
                    _la = self._input.LA(1)
                    if not(_la==SnMsLangParser.T__37 or _la==SnMsLangParser.T__38):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()


                pass
            elif token in [SnMsLangParser.T__39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.match(SnMsLangParser.T__39)
                pass
            elif token in [SnMsLangParser.T__40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 231
                self.match(SnMsLangParser.T__40)
                pass
            elif token in [SnMsLangParser.T__41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 232
                self.match(SnMsLangParser.T__41)
                pass
            elif token in [SnMsLangParser.T__42]:
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
         




