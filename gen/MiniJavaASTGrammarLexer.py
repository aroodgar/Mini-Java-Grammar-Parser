# Generated from F:/IUST_4001/Compiler/HW4/Practical/grammars\MiniJavaASTGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u0143\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\6%\u00f8\n%\r%\16%\u00f9")
        buf.write("\3%\3%\3&\3&\3&\3&\7&\u0102\n&\f&\16&\u0105\13&\3&\3&")
        buf.write("\3&\3&\3&\3\'\3\'\3\'\3\'\7\'\u0110\n\'\f\'\16\'\u0113")
        buf.write("\13\'\3\'\3\'\3(\3(\7(\u0119\n(\f(\16(\u011c\13(\3)\3")
        buf.write(")\3)\5)\u0121\n)\3)\6)\u0124\n)\r)\16)\u0125\3)\5)\u0129")
        buf.write("\n)\5)\u012b\n)\3)\5)\u012e\n)\3*\3*\7*\u0132\n*\f*\16")
        buf.write("*\u0135\13*\3*\5*\u0138\n*\3+\3+\5+\u013c\n+\3,\3,\3,")
        buf.write("\3,\5,\u0142\n,\3\u0103\2-\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S\2U\2W\2\3\2\f\5\2\13\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\3\2\63;\4\2NNnn\3\2\62;\4\2\62;")
        buf.write("aa\6\2&&C\\aac|\4\2\2\u0081\ud802\udc01\3\2\ud802\udc01")
        buf.write("\3\2\udc02\ue001\2\u014d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\3Y\3\2\2\2\5^\3\2\2\2\7e\3\2\2\2\tx\3")
        buf.write("\2\2\2\13\177\3\2\2\2\r\u0084\3\2\2\2\17\u008a\3\2\2\2")
        buf.write("\21\u008e\3\2\2\2\23\u0092\3\2\2\2\25\u0097\3\2\2\2\27")
        buf.write("\u009a\3\2\2\2\31\u00a0\3\2\2\2\33\u00a8\3\2\2\2\35\u00af")
        buf.write("\3\2\2\2\37\u00b4\3\2\2\2!\u00bb\3\2\2\2#\u00c3\3\2\2")
        buf.write("\2%\u00c8\3\2\2\2\'\u00ce\3\2\2\2)\u00d5\3\2\2\2+\u00d7")
        buf.write("\3\2\2\2-\u00d9\3\2\2\2/\u00db\3\2\2\2\61\u00dd\3\2\2")
        buf.write("\2\63\u00df\3\2\2\2\65\u00e1\3\2\2\2\67\u00e3\3\2\2\2")
        buf.write("9\u00e5\3\2\2\2;\u00e7\3\2\2\2=\u00e9\3\2\2\2?\u00ec\3")
        buf.write("\2\2\2A\u00ee\3\2\2\2C\u00f0\3\2\2\2E\u00f2\3\2\2\2G\u00f4")
        buf.write("\3\2\2\2I\u00f7\3\2\2\2K\u00fd\3\2\2\2M\u010b\3\2\2\2")
        buf.write("O\u0116\3\2\2\2Q\u012a\3\2\2\2S\u012f\3\2\2\2U\u013b\3")
        buf.write("\2\2\2W\u0141\3\2\2\2YZ\7o\2\2Z[\7c\2\2[\\\7k\2\2\\]\7")
        buf.write("p\2\2]\4\3\2\2\2^_\7U\2\2_`\7v\2\2`a\7t\2\2ab\7k\2\2b")
        buf.write("c\7p\2\2cd\7i\2\2d\6\3\2\2\2ef\7U\2\2fg\7{\2\2gh\7u\2")
        buf.write("\2hi\7v\2\2ij\7g\2\2jk\7o\2\2kl\7\60\2\2lm\7q\2\2mn\7")
        buf.write("w\2\2no\7v\2\2op\7\60\2\2pq\7r\2\2qr\7t\2\2rs\7k\2\2s")
        buf.write("t\7p\2\2tu\7v\2\2uv\7n\2\2vw\7p\2\2w\b\3\2\2\2xy\7n\2")
        buf.write("\2yz\7g\2\2z{\7p\2\2{|\7i\2\2|}\7v\2\2}~\7j\2\2~\n\3\2")
        buf.write("\2\2\177\u0080\7v\2\2\u0080\u0081\7t\2\2\u0081\u0082\7")
        buf.write("w\2\2\u0082\u0083\7g\2\2\u0083\f\3\2\2\2\u0084\u0085\7")
        buf.write("h\2\2\u0085\u0086\7c\2\2\u0086\u0087\7n\2\2\u0087\u0088")
        buf.write("\7u\2\2\u0088\u0089\7g\2\2\u0089\16\3\2\2\2\u008a\u008b")
        buf.write("\7k\2\2\u008b\u008c\7p\2\2\u008c\u008d\7v\2\2\u008d\20")
        buf.write("\3\2\2\2\u008e\u008f\7p\2\2\u008f\u0090\7g\2\2\u0090\u0091")
        buf.write("\7y\2\2\u0091\22\3\2\2\2\u0092\u0093\7g\2\2\u0093\u0094")
        buf.write("\7n\2\2\u0094\u0095\7u\2\2\u0095\u0096\7g\2\2\u0096\24")
        buf.write("\3\2\2\2\u0097\u0098\7k\2\2\u0098\u0099\7h\2\2\u0099\26")
        buf.write("\3\2\2\2\u009a\u009b\7y\2\2\u009b\u009c\7j\2\2\u009c\u009d")
        buf.write("\7k\2\2\u009d\u009e\7n\2\2\u009e\u009f\7g\2\2\u009f\30")
        buf.write("\3\2\2\2\u00a0\u00a1\7d\2\2\u00a1\u00a2\7q\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7n\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6")
        buf.write("\7c\2\2\u00a6\u00a7\7p\2\2\u00a7\32\3\2\2\2\u00a8\u00a9")
        buf.write("\7r\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac")
        buf.write("\7n\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7e\2\2\u00ae\34")
        buf.write("\3\2\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7j\2\2\u00b1\u00b2")
        buf.write("\7k\2\2\u00b2\u00b3\7u\2\2\u00b3\36\3\2\2\2\u00b4\u00b5")
        buf.write("\7t\2\2\u00b5\u00b6\7g\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8")
        buf.write("\7w\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7p\2\2\u00ba \3")
        buf.write("\2\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd\7z\2\2\u00bd\u00be")
        buf.write("\7v\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1")
        buf.write("\7f\2\2\u00c1\u00c2\7u\2\2\u00c2\"\3\2\2\2\u00c3\u00c4")
        buf.write("\7x\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7$\3\2\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7c\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd")
        buf.write("\7u\2\2\u00cd&\3\2\2\2\u00ce\u00cf\7u\2\2\u00cf\u00d0")
        buf.write("\7v\2\2\u00d0\u00d1\7c\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7k\2\2\u00d3\u00d4\7e\2\2\u00d4(\3\2\2\2\u00d5\u00d6")
        buf.write("\7*\2\2\u00d6*\3\2\2\2\u00d7\u00d8\7+\2\2\u00d8,\3\2\2")
        buf.write("\2\u00d9\u00da\7}\2\2\u00da.\3\2\2\2\u00db\u00dc\7\177")
        buf.write("\2\2\u00dc\60\3\2\2\2\u00dd\u00de\7]\2\2\u00de\62\3\2")
        buf.write("\2\2\u00df\u00e0\7_\2\2\u00e0\64\3\2\2\2\u00e1\u00e2\7")
        buf.write("=\2\2\u00e2\66\3\2\2\2\u00e3\u00e4\7.\2\2\u00e48\3\2\2")
        buf.write("\2\u00e5\u00e6\7\60\2\2\u00e6:\3\2\2\2\u00e7\u00e8\7?")
        buf.write("\2\2\u00e8<\3\2\2\2\u00e9\u00ea\7(\2\2\u00ea\u00eb\7(")
        buf.write("\2\2\u00eb>\3\2\2\2\u00ec\u00ed\7>\2\2\u00ed@\3\2\2\2")
        buf.write("\u00ee\u00ef\7#\2\2\u00efB\3\2\2\2\u00f0\u00f1\7-\2\2")
        buf.write("\u00f1D\3\2\2\2\u00f2\u00f3\7/\2\2\u00f3F\3\2\2\2\u00f4")
        buf.write("\u00f5\7,\2\2\u00f5H\3\2\2\2\u00f6\u00f8\t\2\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\b")
        buf.write("%\2\2\u00fcJ\3\2\2\2\u00fd\u00fe\7\61\2\2\u00fe\u00ff")
        buf.write("\7,\2\2\u00ff\u0103\3\2\2\2\u0100\u0102\13\2\2\2\u0101")
        buf.write("\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0103\u0101\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0103\3")
        buf.write("\2\2\2\u0106\u0107\7,\2\2\u0107\u0108\7\61\2\2\u0108\u0109")
        buf.write("\3\2\2\2\u0109\u010a\b&\2\2\u010aL\3\2\2\2\u010b\u010c")
        buf.write("\7\61\2\2\u010c\u010d\7\61\2\2\u010d\u0111\3\2\2\2\u010e")
        buf.write("\u0110\n\3\2\2\u010f\u010e\3\2\2\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\b\'\2\2\u0115N")
        buf.write("\3\2\2\2\u0116\u011a\5W,\2\u0117\u0119\5U+\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011bP\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u012b\7\62\2\2\u011e\u0128\t\4\2\2\u011f\u0121\5S*\2")
        buf.write("\u0120\u011f\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0129\3")
        buf.write("\2\2\2\u0122\u0124\7a\2\2\u0123\u0122\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0129\5S*\2\u0128\u0120\3\2\2\2\u0128")
        buf.write("\u0123\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u011d\3\2\2\2")
        buf.write("\u012a\u011e\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u012e\t")
        buf.write("\5\2\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012eR")
        buf.write("\3\2\2\2\u012f\u0137\t\6\2\2\u0130\u0132\t\7\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0132\u0135\3\2\2\2\u0133\u0131\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\u0136\3\2\2\2\u0135\u0133\3")
        buf.write("\2\2\2\u0136\u0138\t\6\2\2\u0137\u0133\3\2\2\2\u0137\u0138")
        buf.write("\3\2\2\2\u0138T\3\2\2\2\u0139\u013c\5W,\2\u013a\u013c")
        buf.write("\t\6\2\2\u013b\u0139\3\2\2\2\u013b\u013a\3\2\2\2\u013c")
        buf.write("V\3\2\2\2\u013d\u0142\t\b\2\2\u013e\u0142\n\t\2\2\u013f")
        buf.write("\u0140\t\n\2\2\u0140\u0142\t\13\2\2\u0141\u013d\3\2\2")
        buf.write("\2\u0141\u013e\3\2\2\2\u0141\u013f\3\2\2\2\u0142X\3\2")
        buf.write("\2\2\20\2\u00f9\u0103\u0111\u011a\u0120\u0125\u0128\u012a")
        buf.write("\u012d\u0133\u0137\u013b\u0141\3\2\3\2")
        return buf.getvalue()


class MiniJavaASTGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    INT = 7
    NEW = 8
    ELSE = 9
    IF = 10
    WHILE = 11
    BOOLEAN = 12
    PUBLIC = 13
    THIS = 14
    RETURN = 15
    EXTENDS = 16
    VOID = 17
    CLASS = 18
    STATIC = 19
    LPAREN = 20
    RPAREN = 21
    LBRACE = 22
    RBRACE = 23
    LBRACK = 24
    RBRACK = 25
    SEMI = 26
    COMMA = 27
    DOT = 28
    ASSIGN = 29
    AND = 30
    LT = 31
    BANG = 32
    ADD = 33
    SUB = 34
    MUL = 35
    WS = 36
    COMMENT = 37
    LINE_COMMENT = 38
    IDENTIFIER = 39
    INTEGER_LITERAL = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'String'", "'System.out.println'", "'length'", "'true'", 
            "'false'", "'int'", "'new'", "'else'", "'if'", "'while'", "'boolean'", 
            "'public'", "'this'", "'return'", "'extends'", "'void'", "'class'", 
            "'static'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "'.'", "'='", "'&&'", "'<'", "'!'", "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "NEW", "ELSE", "IF", "WHILE", "BOOLEAN", "PUBLIC", "THIS", 
            "RETURN", "EXTENDS", "VOID", "CLASS", "STATIC", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", 
            "ASSIGN", "AND", "LT", "BANG", "ADD", "SUB", "MUL", "WS", "COMMENT", 
            "LINE_COMMENT", "IDENTIFIER", "INTEGER_LITERAL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "INT", 
                  "NEW", "ELSE", "IF", "WHILE", "BOOLEAN", "PUBLIC", "THIS", 
                  "RETURN", "EXTENDS", "VOID", "CLASS", "STATIC", "LPAREN", 
                  "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", "SEMI", 
                  "COMMA", "DOT", "ASSIGN", "AND", "LT", "BANG", "ADD", 
                  "SUB", "MUL", "WS", "COMMENT", "LINE_COMMENT", "IDENTIFIER", 
                  "INTEGER_LITERAL", "Digits", "LetterOrDigit", "Letter" ]

    grammarFileName = "MiniJavaASTGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


