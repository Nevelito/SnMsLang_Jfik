# Generated from grammar/SnMsLang.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u0173\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\7-\u013d")
        buf.write("\n-\f-\16-\u0140\13-\3.\6.\u0143\n.\r.\16.\u0144\3/\6")
        buf.write("/\u0148\n/\r/\16/\u0149\3/\3/\6/\u014e\n/\r/\16/\u014f")
        buf.write("\3\60\3\60\7\60\u0154\n\60\f\60\16\60\u0157\13\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0166\n\61\3\62\6\62\u0169\n\62\r\62\16\62")
        buf.write("\u016a\3\62\3\62\3\63\3\63\3\63\3\63\3\63\2\2\64\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64\3\2\7\5\2C\\aac|\6\2\62;C")
        buf.write("\\aac|\3\2\62;\5\2\f\f\17\17$$\5\2\13\f\17\17\"\"\2\u0179")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3g\3")
        buf.write("\2\2\2\5i\3\2\2\2\7k\3\2\2\2\tr\3\2\2\2\13t\3\2\2\2\r")
        buf.write("v\3\2\2\2\17~\3\2\2\2\21\u0085\3\2\2\2\23\u008d\3\2\2")
        buf.write("\2\25\u0094\3\2\2\2\27\u009a\3\2\2\2\31\u00a0\3\2\2\2")
        buf.write("\33\u00a2\3\2\2\2\35\u00a4\3\2\2\2\37\u00ac\3\2\2\2!\u00b6")
        buf.write("\3\2\2\2#\u00bc\3\2\2\2%\u00c6\3\2\2\2\'\u00cf\3\2\2\2")
        buf.write(")\u00d7\3\2\2\2+\u00d9\3\2\2\2-\u00db\3\2\2\2/\u00dd\3")
        buf.write("\2\2\2\61\u00df\3\2\2\2\63\u00e1\3\2\2\2\65\u00e3\3\2")
        buf.write("\2\2\67\u00e5\3\2\2\29\u00e8\3\2\2\2;\u00eb\3\2\2\2=\u00ed")
        buf.write("\3\2\2\2?\u00ef\3\2\2\2A\u00f2\3\2\2\2C\u00f5\3\2\2\2")
        buf.write("E\u00f8\3\2\2\2G\u00fa\3\2\2\2I\u00fc\3\2\2\2K\u0103\3")
        buf.write("\2\2\2M\u0116\3\2\2\2O\u0119\3\2\2\2Q\u011c\3\2\2\2S\u0122")
        buf.write("\3\2\2\2U\u0127\3\2\2\2W\u012f\3\2\2\2Y\u013a\3\2\2\2")
        buf.write("[\u0142\3\2\2\2]\u0147\3\2\2\2_\u0151\3\2\2\2a\u0165\3")
        buf.write("\2\2\2c\u0168\3\2\2\2e\u016e\3\2\2\2gh\7?\2\2h\4\3\2\2")
        buf.write("\2ij\7=\2\2j\6\3\2\2\2kl\7y\2\2lm\7{\2\2mn\7r\2\2no\7")
        buf.write("k\2\2op\7u\2\2pq\7|\2\2q\b\3\2\2\2rs\7*\2\2s\n\3\2\2\2")
        buf.write("tu\7+\2\2u\f\3\2\2\2vw\7y\2\2wx\7e\2\2xy\7|\2\2yz\7{\2")
        buf.write("\2z{\7v\2\2{|\7c\2\2|}\7l\2\2}\16\3\2\2\2~\177\7l\2\2")
        buf.write("\177\u0080\7g\2\2\u0080\u0081\7|\2\2\u0081\u0082\7g\2")
        buf.write("\2\u0082\u0083\7n\2\2\u0083\u0084\7k\2\2\u0084\20\3\2")
        buf.write("\2\2\u0085\u0086\7k\2\2\u0086\u0087\7p\2\2\u0087\u0088")
        buf.write("\7c\2\2\u0088\u0089\7e\2\2\u0089\u008a\7|\2\2\u008a\u008b")
        buf.write("\7g\2\2\u008b\u008c\7l\2\2\u008c\22\3\2\2\2\u008d\u008e")
        buf.write("\7f\2\2\u008e\u008f\7q\2\2\u008f\u0090\7r\2\2\u0090\u0091")
        buf.write("\7q\2\2\u0091\u0092\7m\2\2\u0092\u0093\7k\2\2\u0093\24")
        buf.write("\3\2\2\2\u0094\u0095\7|\2\2\u0095\u0096\7y\2\2\u0096\u0097")
        buf.write("\7t\2\2\u0097\u0098\7q\2\2\u0098\u0099\7e\2\2\u0099\26")
        buf.write("\3\2\2\2\u009a\u009b\7{\2\2\u009b\u009c\7k\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f\7f\2\2\u009f\30")
        buf.write("\3\2\2\2\u00a0\u00a1\7}\2\2\u00a1\32\3\2\2\2\u00a2\u00a3")
        buf.write("\7\177\2\2\u00a3\34\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5\u00a6")
        buf.write("\7w\2\2\u00a6\u00a7\7p\2\2\u00a7\u00a8\7m\2\2\u00a8\u00a9")
        buf.write("\7e\2\2\u00a9\u00aa\7l\2\2\u00aa\u00ab\7c\2\2\u00ab\36")
        buf.write("\3\2\2\2\u00ac\u00ad\7i\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7g\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2")
        buf.write("\7c\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4\7q\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5 \3\2\2\2\u00b6\u00b7\7m\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7c\2\2\u00b9\u00ba\7u\2\2\u00ba\u00bb")
        buf.write("\7c\2\2\u00bb\"\3\2\2\2\u00bc\u00bd\7u\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1")
        buf.write("\7m\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4")
        buf.write("\7t\2\2\u00c4\u00c5\7c\2\2\u00c5$\3\2\2\2\u00c6\u00c7")
        buf.write("\7i\2\2\u00c7\u00c8\7n\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7d\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7n\2\2\u00cc\u00cd")
        buf.write("\7p\2\2\u00cd\u00ce\7c\2\2\u00ce&\3\2\2\2\u00cf\u00d0")
        buf.write("\7n\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2\7m\2\2\u00d2\u00d3")
        buf.write("\7c\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7p\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6(\3\2\2\2\u00d7\u00d8\7]\2\2\u00d8*\3\2\2")
        buf.write("\2\u00d9\u00da\7.\2\2\u00da,\3\2\2\2\u00db\u00dc\7_\2")
        buf.write("\2\u00dc.\3\2\2\2\u00dd\u00de\7,\2\2\u00de\60\3\2\2\2")
        buf.write("\u00df\u00e0\7\61\2\2\u00e0\62\3\2\2\2\u00e1\u00e2\7-")
        buf.write("\2\2\u00e2\64\3\2\2\2\u00e3\u00e4\7/\2\2\u00e4\66\3\2")
        buf.write("\2\2\u00e5\u00e6\7?\2\2\u00e6\u00e7\7?\2\2\u00e78\3\2")
        buf.write("\2\2\u00e8\u00e9\7#\2\2\u00e9\u00ea\7?\2\2\u00ea:\3\2")
        buf.write("\2\2\u00eb\u00ec\7>\2\2\u00ec<\3\2\2\2\u00ed\u00ee\7@")
        buf.write("\2\2\u00ee>\3\2\2\2\u00ef\u00f0\7>\2\2\u00f0\u00f1\7@")
        buf.write("\2\2\u00f1@\3\2\2\2\u00f2\u00f3\7(\2\2\u00f3\u00f4\7(")
        buf.write("\2\2\u00f4B\3\2\2\2\u00f5\u00f6\7~\2\2\u00f6\u00f7\7~")
        buf.write("\2\2\u00f7D\3\2\2\2\u00f8\u00f9\7`\2\2\u00f9F\3\2\2\2")
        buf.write("\u00fa\u00fb\7#\2\2\u00fbH\3\2\2\2\u00fc\u00fd\7n\2\2")
        buf.write("\u00fd\u00fe\7k\2\2\u00fe\u00ff\7e\2\2\u00ff\u0100\7|")
        buf.write("\2\2\u0100\u0101\7d\2\2\u0101\u0102\7c\2\2\u0102J\3\2")
        buf.write("\2\2\u0103\u0104\7|\2\2\u0104\u0105\7o\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7g\2\2\u0107\u0108\7p\2\2\u0108\u0109")
        buf.write("\7p\2\2\u0109\u010a\7q\2\2\u010a\u010b\7r\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010c\u010d\7|\2\2\u010d\u010e\7g\2\2\u010e\u010f")
        buf.write("\7e\2\2\u010f\u0110\7k\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7m\2\2\u0112\u0113\7q\2\2\u0113\u0114\7y\2\2\u0114\u0115")
        buf.write("\7c\2\2\u0115L\3\2\2\2\u0116\u0117\7\65\2\2\u0117\u0118")
        buf.write("\7\64\2\2\u0118N\3\2\2\2\u0119\u011a\78\2\2\u011a\u011b")
        buf.write("\7\66\2\2\u011bP\3\2\2\2\u011c\u011d\7v\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\u011f\7m\2\2\u011f\u0120\7u\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121R\3\2\2\2\u0122\u0123\7d\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7q\2\2\u0125\u0126\7n\2\2\u0126T\3")
        buf.write("\2\2\2\u0127\u0128\7|\2\2\u0128\u0129\7o\2\2\u0129\u012a")
        buf.write("\7k\2\2\u012a\u012b\7g\2\2\u012b\u012c\7p\2\2\u012c\u012d")
        buf.write("\7p\2\2\u012d\u012e\7c\2\2\u012eV\3\2\2\2\u012f\u0130")
        buf.write("\7f\2\2\u0130\u0131\7{\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7o\2\2\u0134\u0135\7k\2\2\u0135\u0136")
        buf.write("\7e\2\2\u0136\u0137\7|\2\2\u0137\u0138\7p\2\2\u0138\u0139")
        buf.write("\7{\2\2\u0139X\3\2\2\2\u013a\u013e\t\2\2\2\u013b\u013d")
        buf.write("\t\3\2\2\u013c\u013b\3\2\2\2\u013d\u0140\3\2\2\2\u013e")
        buf.write("\u013c\3\2\2\2\u013e\u013f\3\2\2\2\u013fZ\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0141\u0143\t\4\2\2\u0142\u0141\3\2\2\2")
        buf.write("\u0143\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144\u0145\3")
        buf.write("\2\2\2\u0145\\\3\2\2\2\u0146\u0148\t\4\2\2\u0147\u0146")
        buf.write("\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\7\60\2")
        buf.write("\2\u014c\u014e\t\4\2\2\u014d\u014c\3\2\2\2\u014e\u014f")
        buf.write("\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150")
        buf.write("^\3\2\2\2\u0151\u0155\7$\2\2\u0152\u0154\n\5\2\2\u0153")
        buf.write("\u0152\3\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2")
        buf.write("\u0155\u0156\3\2\2\2\u0156\u0158\3\2\2\2\u0157\u0155\3")
        buf.write("\2\2\2\u0158\u0159\7$\2\2\u0159`\3\2\2\2\u015a\u015b\7")
        buf.write("r\2\2\u015b\u015c\7t\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7y\2\2\u015e\u015f\7f\2\2\u015f\u0166\7c\2\2\u0160\u0161")
        buf.write("\7h\2\2\u0161\u0162\7c\2\2\u0162\u0163\7n\2\2\u0163\u0164")
        buf.write("\7u\2\2\u0164\u0166\7|\2\2\u0165\u015a\3\2\2\2\u0165\u0160")
        buf.write("\3\2\2\2\u0166b\3\2\2\2\u0167\u0169\t\6\2\2\u0168\u0167")
        buf.write("\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\b\62\2")
        buf.write("\2\u016dd\3\2\2\2\u016e\u016f\13\2\2\2\u016f\u0170\b\63")
        buf.write("\3\2\u0170\u0171\3\2\2\2\u0171\u0172\b\63\2\2\u0172f\3")
        buf.write("\2\2\2\n\2\u013e\u0144\u0149\u014f\u0155\u0165\u016a\4")
        buf.write("\b\2\2\3\63\2")
        return buf.getvalue()


class SnMsLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    ID = 44
    INT = 45
    FLOAT = 46
    STRING = 47
    BOOL = 48
    WS = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'wypisz'", "'('", "')'", "'wczytaj'", "'jezeli'", 
            "'inaczej'", "'dopoki'", "'zwroc'", "'yield'", "'{'", "'}'", 
            "'funkcja'", "'generator'", "'klasa'", "'struktura'", "'globalna'", 
            "'lokalna'", "'['", "','", "']'", "'*'", "'/'", "'+'", "'-'", 
            "'=='", "'!='", "'<'", "'>'", "'<>'", "'&&'", "'||'", "'^'", 
            "'!'", "'liczba'", "'zmiennoprzecinkowa'", "'32'", "'64'", "'tekst'", 
            "'bool'", "'zmienna'", "'dynamiczny'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "FLOAT", "STRING", "BOOL", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "ID", "INT", 
                  "FLOAT", "STRING", "BOOL", "WS", "ERROR_CHAR" ]

    grammarFileName = "SnMsLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            System.err.println("Nieoczekiwany znak: " + getText());
     


