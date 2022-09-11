# Generated from F:/IUST_4001/Compiler/HW4/Practical/grammars\MiniJavaASTGrammar.g4 by ANTLR 4.9.1
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u00da\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\7\2\27\n\2\f\2\16\2\32")
        buf.write("\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\3\4\7\4>\n\4\f\4")
        buf.write("\16\4A\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\7\5O\n\5\f\5\16\5R\13\5\5\5T\n\5\3\5\3\5\3\5\7")
        buf.write("\5Y\n\5\f\5\16\5\\\13\5\3\5\7\5_\n\5\f\5\16\5b\13\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7r\n\7\3\b\3\b\7\bv\n\b\f\b\16\by\13\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\5\b\u009d\n\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\5\t\u00b6\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t\u00ca")
        buf.write("\n\t\f\t\16\t\u00cd\13\t\5\t\u00cf\n\t\3\t\3\t\7\t\u00d3")
        buf.write("\n\t\f\t\16\t\u00d6\13\t\3\n\3\n\3\n\2\3\20\13\2\4\6\b")
        buf.write("\n\f\16\20\22\2\3\4\2 !#%\2\u00ee\2\24\3\2\2\2\4\35\3")
        buf.write("\2\2\2\6/\3\2\2\2\bD\3\2\2\2\nh\3\2\2\2\fq\3\2\2\2\16")
        buf.write("\u009c\3\2\2\2\20\u00b5\3\2\2\2\22\u00d7\3\2\2\2\24\30")
        buf.write("\5\4\3\2\25\27\5\6\4\2\26\25\3\2\2\2\27\32\3\2\2\2\30")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2")
        buf.write("\33\34\7\2\2\3\34\3\3\2\2\2\35\36\7\24\2\2\36\37\5\22")
        buf.write("\n\2\37 \7\30\2\2 !\7\17\2\2!\"\7\25\2\2\"#\7\23\2\2#")
        buf.write("$\7\3\2\2$%\7\26\2\2%&\7\4\2\2&\'\7\32\2\2\'(\7\33\2\2")
        buf.write("()\5\22\n\2)*\7\27\2\2*+\7\30\2\2+,\5\16\b\2,-\7\31\2")
        buf.write("\2-.\7\31\2\2.\5\3\2\2\2/\60\7\24\2\2\60\63\5\22\n\2\61")
        buf.write("\62\7\22\2\2\62\64\5\22\n\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\65\3\2\2\2\659\7\30\2\2\668\5\n\6\2\67\66\3\2\2")
        buf.write("\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:?\3\2\2\2;9\3\2\2\2")
        buf.write("<>\5\b\5\2=<\3\2\2\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@B\3")
        buf.write("\2\2\2A?\3\2\2\2BC\7\31\2\2C\7\3\2\2\2DE\7\17\2\2EF\5")
        buf.write("\f\7\2FG\5\22\n\2GS\7\26\2\2HI\5\f\7\2IP\5\22\n\2JK\7")
        buf.write("\35\2\2KL\5\f\7\2LM\5\22\n\2MO\3\2\2\2NJ\3\2\2\2OR\3\2")
        buf.write("\2\2PN\3\2\2\2PQ\3\2\2\2QT\3\2\2\2RP\3\2\2\2SH\3\2\2\2")
        buf.write("ST\3\2\2\2TU\3\2\2\2UV\7\27\2\2VZ\7\30\2\2WY\5\n\6\2X")
        buf.write("W\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[`\3\2\2\2\\Z")
        buf.write("\3\2\2\2]_\5\16\b\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3")
        buf.write("\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7\21\2\2de\5\20\t\2ef\7\34")
        buf.write("\2\2fg\7\31\2\2g\t\3\2\2\2hi\5\f\7\2ij\5\22\n\2jk\7\34")
        buf.write("\2\2k\13\3\2\2\2lm\7\t\2\2mn\7\32\2\2nr\7\33\2\2or\7\16")
        buf.write("\2\2pr\7\t\2\2ql\3\2\2\2qo\3\2\2\2qp\3\2\2\2r\r\3\2\2")
        buf.write("\2sw\7\30\2\2tv\5\16\b\2ut\3\2\2\2vy\3\2\2\2wu\3\2\2\2")
        buf.write("wx\3\2\2\2xz\3\2\2\2yw\3\2\2\2z\u009d\7\31\2\2{|\7\f\2")
        buf.write("\2|}\7\26\2\2}~\5\20\t\2~\177\7\27\2\2\177\u0080\5\16")
        buf.write("\b\2\u0080\u0081\7\13\2\2\u0081\u0082\5\16\b\2\u0082\u009d")
        buf.write("\3\2\2\2\u0083\u0084\7\r\2\2\u0084\u0085\7\26\2\2\u0085")
        buf.write("\u0086\5\20\t\2\u0086\u0087\7\27\2\2\u0087\u0088\5\16")
        buf.write("\b\2\u0088\u009d\3\2\2\2\u0089\u008a\7\5\2\2\u008a\u008b")
        buf.write("\7\26\2\2\u008b\u008c\5\20\t\2\u008c\u008d\7\27\2\2\u008d")
        buf.write("\u008e\7\34\2\2\u008e\u009d\3\2\2\2\u008f\u0090\5\22\n")
        buf.write("\2\u0090\u0091\7\37\2\2\u0091\u0092\5\20\t\2\u0092\u0093")
        buf.write("\7\34\2\2\u0093\u009d\3\2\2\2\u0094\u0095\5\22\n\2\u0095")
        buf.write("\u0096\7\32\2\2\u0096\u0097\5\20\t\2\u0097\u0098\7\33")
        buf.write("\2\2\u0098\u0099\7\37\2\2\u0099\u009a\5\20\t\2\u009a\u009b")
        buf.write("\7\34\2\2\u009b\u009d\3\2\2\2\u009cs\3\2\2\2\u009c{\3")
        buf.write("\2\2\2\u009c\u0083\3\2\2\2\u009c\u0089\3\2\2\2\u009c\u008f")
        buf.write("\3\2\2\2\u009c\u0094\3\2\2\2\u009d\17\3\2\2\2\u009e\u009f")
        buf.write("\b\t\1\2\u009f\u00b6\7*\2\2\u00a0\u00b6\7\7\2\2\u00a1")
        buf.write("\u00b6\7\b\2\2\u00a2\u00b6\5\22\n\2\u00a3\u00b6\7\20\2")
        buf.write("\2\u00a4\u00a5\7\n\2\2\u00a5\u00a6\7\t\2\2\u00a6\u00a7")
        buf.write("\7\32\2\2\u00a7\u00a8\5\20\t\2\u00a8\u00a9\7\33\2\2\u00a9")
        buf.write("\u00b6\3\2\2\2\u00aa\u00ab\7\n\2\2\u00ab\u00ac\5\22\n")
        buf.write("\2\u00ac\u00ad\7\26\2\2\u00ad\u00ae\7\27\2\2\u00ae\u00b6")
        buf.write("\3\2\2\2\u00af\u00b0\7\"\2\2\u00b0\u00b6\5\20\t\4\u00b1")
        buf.write("\u00b2\7\26\2\2\u00b2\u00b3\5\20\t\2\u00b3\u00b4\7\27")
        buf.write("\2\2\u00b4\u00b6\3\2\2\2\u00b5\u009e\3\2\2\2\u00b5\u00a0")
        buf.write("\3\2\2\2\u00b5\u00a1\3\2\2\2\u00b5\u00a2\3\2\2\2\u00b5")
        buf.write("\u00a3\3\2\2\2\u00b5\u00a4\3\2\2\2\u00b5\u00aa\3\2\2\2")
        buf.write("\u00b5\u00af\3\2\2\2\u00b5\u00b1\3\2\2\2\u00b6\u00d4\3")
        buf.write("\2\2\2\u00b7\u00b8\f\17\2\2\u00b8\u00b9\t\2\2\2\u00b9")
        buf.write("\u00d3\5\20\t\20\u00ba\u00bb\f\16\2\2\u00bb\u00bc\7\32")
        buf.write("\2\2\u00bc\u00bd\5\20\t\2\u00bd\u00be\7\33\2\2\u00be\u00d3")
        buf.write("\3\2\2\2\u00bf\u00c0\f\r\2\2\u00c0\u00c1\7\36\2\2\u00c1")
        buf.write("\u00d3\7\6\2\2\u00c2\u00c3\f\f\2\2\u00c3\u00c4\7\36\2")
        buf.write("\2\u00c4\u00c5\5\22\n\2\u00c5\u00ce\7\26\2\2\u00c6\u00cb")
        buf.write("\5\20\t\2\u00c7\u00c8\7\35\2\2\u00c8\u00ca\5\20\t\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2")
        buf.write("\u00cb\u00cc\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd\u00cb\3")
        buf.write("\2\2\2\u00ce\u00c6\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d1\7\27\2\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00b7\3\2\2\2\u00d2\u00ba\3\2\2\2\u00d2\u00bf\3\2\2\2")
        buf.write("\u00d2\u00c2\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\21\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d7\u00d8\7)\2\2\u00d8\23\3\2\2\2\22\30\63")
        buf.write("9?PSZ`qw\u009c\u00b5\u00cb\u00ce\u00d2\u00d4")
        return buf.getvalue()


class MiniJavaASTGrammarParser ( Parser ):

    grammarFileName = "MiniJavaASTGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'String'", "'System.out.println'", 
                     "'length'", "'true'", "'false'", "'int'", "'new'", 
                     "'else'", "'if'", "'while'", "'boolean'", "'public'", 
                     "'this'", "'return'", "'extends'", "'void'", "'class'", 
                     "'static'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "'.'", "'='", "'&&'", "'<'", "'!'", "'+'", 
                     "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "NEW", 
                      "ELSE", "IF", "WHILE", "BOOLEAN", "PUBLIC", "THIS", 
                      "RETURN", "EXTENDS", "VOID", "CLASS", "STATIC", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
                      "SEMI", "COMMA", "DOT", "ASSIGN", "AND", "LT", "BANG", 
                      "ADD", "SUB", "MUL", "WS", "COMMENT", "LINE_COMMENT", 
                      "IDENTIFIER", "INTEGER_LITERAL" ]

    RULE_program = 0
    RULE_mainClass = 1
    RULE_classDeclaration = 2
    RULE_methodDeclaration = 3
    RULE_varDeclaration = 4
    RULE_type = 5
    RULE_statement = 6
    RULE_expression = 7
    RULE_identifier = 8

    ruleNames =  [ "program", "mainClass", "classDeclaration", "methodDeclaration", 
                   "varDeclaration", "type", "statement", "expression", 
                   "identifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    INT=7
    NEW=8
    ELSE=9
    IF=10
    WHILE=11
    BOOLEAN=12
    PUBLIC=13
    THIS=14
    RETURN=15
    EXTENDS=16
    VOID=17
    CLASS=18
    STATIC=19
    LPAREN=20
    RPAREN=21
    LBRACE=22
    RBRACE=23
    LBRACK=24
    RBRACK=25
    SEMI=26
    COMMA=27
    DOT=28
    ASSIGN=29
    AND=30
    LT=31
    BANG=32
    ADD=33
    SUB=34
    MUL=35
    WS=36
    COMMENT=37
    LINE_COMMENT=38
    IDENTIFIER=39
    INTEGER_LITERAL=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def mainClass(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.MainClassContext,0)


        def EOF(self):
            return self.getToken(MiniJavaASTGrammarParser.EOF, 0)

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniJavaASTGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.mainClass()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaASTGrammarParser.CLASS:
                self.state = 19
                self.classDeclaration()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 25
            self.match(MiniJavaASTGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def CLASS(self):
            return self.getToken(MiniJavaASTGrammarParser.CLASS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaASTGrammarParser.LBRACE)
            else:
                return self.getToken(MiniJavaASTGrammarParser.LBRACE, i)

        def PUBLIC(self):
            return self.getToken(MiniJavaASTGrammarParser.PUBLIC, 0)

        def STATIC(self):
            return self.getToken(MiniJavaASTGrammarParser.STATIC, 0)

        def VOID(self):
            return self.getToken(MiniJavaASTGrammarParser.VOID, 0)

        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)

        def LBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACK, 0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.StatementContext,0)


        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaASTGrammarParser.RBRACE)
            else:
                return self.getToken(MiniJavaASTGrammarParser.RBRACE, i)

        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_mainClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainClass" ):
                listener.enterMainClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainClass" ):
                listener.exitMainClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainClass" ):
                return visitor.visitMainClass(self)
            else:
                return visitor.visitChildren(self)




    def mainClass(self):

        localctx = MiniJavaASTGrammarParser.MainClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainClass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MiniJavaASTGrammarParser.CLASS)
            self.state = 28
            self.identifier()
            self.state = 29
            self.match(MiniJavaASTGrammarParser.LBRACE)
            self.state = 30
            self.match(MiniJavaASTGrammarParser.PUBLIC)
            self.state = 31
            self.match(MiniJavaASTGrammarParser.STATIC)
            self.state = 32
            self.match(MiniJavaASTGrammarParser.VOID)
            self.state = 33
            self.match(MiniJavaASTGrammarParser.T__0)
            self.state = 34
            self.match(MiniJavaASTGrammarParser.LPAREN)
            self.state = 35
            self.match(MiniJavaASTGrammarParser.T__1)
            self.state = 36
            self.match(MiniJavaASTGrammarParser.LBRACK)
            self.state = 37
            self.match(MiniJavaASTGrammarParser.RBRACK)
            self.state = 38
            self.identifier()
            self.state = 39
            self.match(MiniJavaASTGrammarParser.RPAREN)
            self.state = 40
            self.match(MiniJavaASTGrammarParser.LBRACE)
            self.state = 41
            self.statement()
            self.state = 42
            self.match(MiniJavaASTGrammarParser.RBRACE)
            self.state = 43
            self.match(MiniJavaASTGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def CLASS(self):
            return self.getToken(MiniJavaASTGrammarParser.CLASS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,i)


        def LBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACE, 0)

        def EXTENDS(self):
            return self.getToken(MiniJavaASTGrammarParser.EXTENDS, 0)

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.VarDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = MiniJavaASTGrammarParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(MiniJavaASTGrammarParser.CLASS)
            self.state = 46
            self.identifier()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniJavaASTGrammarParser.EXTENDS:
                self.state = 47
                self.match(MiniJavaASTGrammarParser.EXTENDS)
                self.state = 48
                self.identifier()


            self.state = 51
            self.match(MiniJavaASTGrammarParser.LBRACE)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaASTGrammarParser.INT or _la==MiniJavaASTGrammarParser.BOOLEAN:
                self.state = 52
                self.varDeclaration()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaASTGrammarParser.PUBLIC:
                self.state = 58
                self.methodDeclaration()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(MiniJavaASTGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def PUBLIC(self):
            return self.getToken(MiniJavaASTGrammarParser.PUBLIC, 0)

        def type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.TypeContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.TypeContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,i)


        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACE, 0)

        def RETURN(self):
            return self.getToken(MiniJavaASTGrammarParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniJavaASTGrammarParser.SEMI, 0)

        def RBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACE, 0)

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.VarDeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.StatementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaASTGrammarParser.COMMA)
            else:
                return self.getToken(MiniJavaASTGrammarParser.COMMA, i)

        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = MiniJavaASTGrammarParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MiniJavaASTGrammarParser.PUBLIC)
            self.state = 67
            self.type()
            self.state = 68
            self.identifier()
            self.state = 69
            self.match(MiniJavaASTGrammarParser.LPAREN)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniJavaASTGrammarParser.INT or _la==MiniJavaASTGrammarParser.BOOLEAN:
                self.state = 70
                self.type()
                self.state = 71
                self.identifier()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniJavaASTGrammarParser.COMMA:
                    self.state = 72
                    self.match(MiniJavaASTGrammarParser.COMMA)
                    self.state = 73
                    self.type()
                    self.state = 74
                    self.identifier()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 83
            self.match(MiniJavaASTGrammarParser.RPAREN)
            self.state = 84
            self.match(MiniJavaASTGrammarParser.LBRACE)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaASTGrammarParser.INT or _la==MiniJavaASTGrammarParser.BOOLEAN:
                self.state = 85
                self.varDeclaration()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaASTGrammarParser.T__2) | (1 << MiniJavaASTGrammarParser.IF) | (1 << MiniJavaASTGrammarParser.WHILE) | (1 << MiniJavaASTGrammarParser.LBRACE) | (1 << MiniJavaASTGrammarParser.IDENTIFIER))) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MiniJavaASTGrammarParser.RETURN)
            self.state = 98
            self.expression(0)
            self.state = 99
            self.match(MiniJavaASTGrammarParser.SEMI)
            self.state = 100
            self.match(MiniJavaASTGrammarParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def type(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.TypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(MiniJavaASTGrammarParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniJavaASTGrammarParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.type()
            self.state = 103
            self.identifier()
            self.state = 104
            self.match(MiniJavaASTGrammarParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()


        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr
            self.name_attr = ctx.name_attr



    class Type2Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniJavaASTGrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType2" ):
                listener.enterType2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType2" ):
                listener.exitType2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType2" ):
                return visitor.visitType2(self)
            else:
                return visitor.visitChildren(self)


    class Type1Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(MiniJavaASTGrammarParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType1" ):
                listener.enterType1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType1" ):
                listener.exitType1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType1" ):
                return visitor.visitType1(self)
            else:
                return visitor.visitChildren(self)


    class Type0Context(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MiniJavaASTGrammarParser.INT, 0)
        def LBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType0" ):
                listener.enterType0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType0" ):
                listener.exitType0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType0" ):
                return visitor.visitType0(self)
            else:
                return visitor.visitChildren(self)



    def type(self):

        localctx = MiniJavaASTGrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = MiniJavaASTGrammarParser.Type0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(MiniJavaASTGrammarParser.INT)
                self.state = 107
                self.match(MiniJavaASTGrammarParser.LBRACK)
                self.state = 108
                self.match(MiniJavaASTGrammarParser.RBRACK)
                pass

            elif la_ == 2:
                localctx = MiniJavaASTGrammarParser.Type1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(MiniJavaASTGrammarParser.BOOLEAN)
                pass

            elif la_ == 3:
                localctx = MiniJavaASTGrammarParser.Type2Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(MiniJavaASTGrammarParser.INT)
                pass


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
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()


        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr
            self.name_attr = ctx.name_attr



    class Statement5Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)

        def LBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACK, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,i)

        def RBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACK, 0)
        def ASSIGN(self):
            return self.getToken(MiniJavaASTGrammarParser.ASSIGN, 0)
        def SEMI(self):
            return self.getToken(MiniJavaASTGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement5" ):
                listener.enterStatement5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement5" ):
                listener.exitStatement5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement5" ):
                return visitor.visitStatement5(self)
            else:
                return visitor.visitChildren(self)


    class Statement3Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)
        def SEMI(self):
            return self.getToken(MiniJavaASTGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement3" ):
                listener.enterStatement3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement3" ):
                listener.exitStatement3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement3" ):
                return visitor.visitStatement3(self)
            else:
                return visitor.visitChildren(self)


    class Statement4Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)

        def ASSIGN(self):
            return self.getToken(MiniJavaASTGrammarParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def SEMI(self):
            return self.getToken(MiniJavaASTGrammarParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement4" ):
                listener.enterStatement4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement4" ):
                listener.exitStatement4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement4" ):
                return visitor.visitStatement4(self)
            else:
                return visitor.visitChildren(self)


    class Statement1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(MiniJavaASTGrammarParser.IF, 0)
        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(MiniJavaASTGrammarParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement1" ):
                listener.enterStatement1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement1" ):
                listener.exitStatement1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement1" ):
                return visitor.visitStatement1(self)
            else:
                return visitor.visitChildren(self)


    class Statement2Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(MiniJavaASTGrammarParser.WHILE, 0)
        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)
        def statement(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement2" ):
                listener.enterStatement2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement2" ):
                listener.exitStatement2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement2" ):
                return visitor.visitStatement2(self)
            else:
                return visitor.visitChildren(self)


    class Statement0Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACE, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement0" ):
                listener.enterStatement0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement0" ):
                listener.exitStatement0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement0" ):
                return visitor.visitStatement0(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MiniJavaASTGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = MiniJavaASTGrammarParser.Statement0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(MiniJavaASTGrammarParser.LBRACE)
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaASTGrammarParser.T__2) | (1 << MiniJavaASTGrammarParser.IF) | (1 << MiniJavaASTGrammarParser.WHILE) | (1 << MiniJavaASTGrammarParser.LBRACE) | (1 << MiniJavaASTGrammarParser.IDENTIFIER))) != 0):
                    self.state = 114
                    self.statement()
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 120
                self.match(MiniJavaASTGrammarParser.RBRACE)
                pass

            elif la_ == 2:
                localctx = MiniJavaASTGrammarParser.Statement1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.match(MiniJavaASTGrammarParser.IF)
                self.state = 122
                self.match(MiniJavaASTGrammarParser.LPAREN)
                self.state = 123
                self.expression(0)
                self.state = 124
                self.match(MiniJavaASTGrammarParser.RPAREN)
                self.state = 125
                self.statement()
                self.state = 126
                self.match(MiniJavaASTGrammarParser.ELSE)
                self.state = 127
                self.statement()
                pass

            elif la_ == 3:
                localctx = MiniJavaASTGrammarParser.Statement2Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.match(MiniJavaASTGrammarParser.WHILE)
                self.state = 130
                self.match(MiniJavaASTGrammarParser.LPAREN)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(MiniJavaASTGrammarParser.RPAREN)
                self.state = 133
                self.statement()
                pass

            elif la_ == 4:
                localctx = MiniJavaASTGrammarParser.Statement3Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(MiniJavaASTGrammarParser.T__2)
                self.state = 136
                self.match(MiniJavaASTGrammarParser.LPAREN)
                self.state = 137
                self.expression(0)
                self.state = 138
                self.match(MiniJavaASTGrammarParser.RPAREN)
                self.state = 139
                self.match(MiniJavaASTGrammarParser.SEMI)
                pass

            elif la_ == 5:
                localctx = MiniJavaASTGrammarParser.Statement4Context(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.identifier()
                self.state = 142
                self.match(MiniJavaASTGrammarParser.ASSIGN)
                self.state = 143
                self.expression(0)
                self.state = 144
                self.match(MiniJavaASTGrammarParser.SEMI)
                pass

            elif la_ == 6:
                localctx = MiniJavaASTGrammarParser.Statement5Context(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 146
                self.identifier()
                self.state = 147
                self.match(MiniJavaASTGrammarParser.LBRACK)
                self.state = 148
                self.expression(0)
                self.state = 149
                self.match(MiniJavaASTGrammarParser.RBRACK)
                self.state = 150
                self.match(MiniJavaASTGrammarParser.ASSIGN)
                self.state = 151
                self.expression(0)
                self.state = 152
                self.match(MiniJavaASTGrammarParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()


        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr
            self.name_attr = ctx.name_attr


    class Expression6Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression6" ):
                listener.enterExpression6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression6" ):
                listener.exitExpression6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)


    class Expression7Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression7" ):
                listener.enterExpression7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression7" ):
                listener.exitExpression7(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)


    class Expression4Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniJavaASTGrammarParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression4" ):
                listener.enterExpression4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression4" ):
                listener.exitExpression4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)


    class Expression5Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression5" ):
                listener.enterExpression5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression5" ):
                listener.exitExpression5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)


    class Expression2Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def DOT(self):
            return self.getToken(MiniJavaASTGrammarParser.DOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression2" ):
                listener.enterExpression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression2" ):
                listener.exitExpression2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)


    class Expression3Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,i)

        def DOT(self):
            return self.getToken(MiniJavaASTGrammarParser.DOT, 0)
        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)

        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaASTGrammarParser.COMMA)
            else:
                return self.getToken(MiniJavaASTGrammarParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression3" ):
                listener.enterExpression3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression3" ):
                listener.exitExpression3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)


    class Expression0Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(MiniJavaASTGrammarParser.AND, 0)
        def LT(self):
            return self.getToken(MiniJavaASTGrammarParser.LT, 0)
        def ADD(self):
            return self.getToken(MiniJavaASTGrammarParser.ADD, 0)
        def SUB(self):
            return self.getToken(MiniJavaASTGrammarParser.SUB, 0)
        def MUL(self):
            return self.getToken(MiniJavaASTGrammarParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression0" ):
                listener.enterExpression0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression0" ):
                listener.exitExpression0(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression0" ):
                return visitor.visitExpression0(self)
            else:
                return visitor.visitChildren(self)


    class Expression1Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaASTGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,i)

        def LBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression1" ):
                listener.enterExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression1" ):
                listener.exitExpression1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)


    class Expression8Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THIS(self):
            return self.getToken(MiniJavaASTGrammarParser.THIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression8" ):
                listener.enterExpression8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression8" ):
                listener.exitExpression8(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)


    class Expression10Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(MiniJavaASTGrammarParser.NEW, 0)
        def identifier(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.IdentifierContext,0)

        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression10" ):
                listener.enterExpression10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression10" ):
                listener.exitExpression10(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)


    class Expression9Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(MiniJavaASTGrammarParser.NEW, 0)
        def INT(self):
            return self.getToken(MiniJavaASTGrammarParser.INT, 0)
        def LBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.LBRACK, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def RBRACK(self):
            return self.getToken(MiniJavaASTGrammarParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression9" ):
                listener.enterExpression9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression9" ):
                listener.exitExpression9(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)


    class Expression12Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(MiniJavaASTGrammarParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression12" ):
                listener.enterExpression12(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression12" ):
                listener.exitExpression12(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression12" ):
                return visitor.visitExpression12(self)
            else:
                return visitor.visitChildren(self)


    class Expression11Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaASTGrammarParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BANG(self):
            return self.getToken(MiniJavaASTGrammarParser.BANG, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaASTGrammarParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression11" ):
                listener.enterExpression11(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression11" ):
                listener.exitExpression11(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniJavaASTGrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MiniJavaASTGrammarParser.Expression4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 157
                self.match(MiniJavaASTGrammarParser.INTEGER_LITERAL)
                pass

            elif la_ == 2:
                localctx = MiniJavaASTGrammarParser.Expression5Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(MiniJavaASTGrammarParser.T__4)
                pass

            elif la_ == 3:
                localctx = MiniJavaASTGrammarParser.Expression6Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(MiniJavaASTGrammarParser.T__5)
                pass

            elif la_ == 4:
                localctx = MiniJavaASTGrammarParser.Expression7Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.identifier()
                pass

            elif la_ == 5:
                localctx = MiniJavaASTGrammarParser.Expression8Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(MiniJavaASTGrammarParser.THIS)
                pass

            elif la_ == 6:
                localctx = MiniJavaASTGrammarParser.Expression9Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.match(MiniJavaASTGrammarParser.NEW)
                self.state = 163
                self.match(MiniJavaASTGrammarParser.INT)
                self.state = 164
                self.match(MiniJavaASTGrammarParser.LBRACK)
                self.state = 165
                self.expression(0)
                self.state = 166
                self.match(MiniJavaASTGrammarParser.RBRACK)
                pass

            elif la_ == 7:
                localctx = MiniJavaASTGrammarParser.Expression10Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(MiniJavaASTGrammarParser.NEW)
                self.state = 169
                self.identifier()
                self.state = 170
                self.match(MiniJavaASTGrammarParser.LPAREN)
                self.state = 171
                self.match(MiniJavaASTGrammarParser.RPAREN)
                pass

            elif la_ == 8:
                localctx = MiniJavaASTGrammarParser.Expression11Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.match(MiniJavaASTGrammarParser.BANG)
                self.state = 174
                self.expression(2)
                pass

            elif la_ == 9:
                localctx = MiniJavaASTGrammarParser.Expression12Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(MiniJavaASTGrammarParser.LPAREN)
                self.state = 176
                self.expression(0)
                self.state = 177
                self.match(MiniJavaASTGrammarParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaASTGrammarParser.Expression0Context(self, MiniJavaASTGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 181
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 182
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaASTGrammarParser.AND) | (1 << MiniJavaASTGrammarParser.LT) | (1 << MiniJavaASTGrammarParser.ADD) | (1 << MiniJavaASTGrammarParser.SUB) | (1 << MiniJavaASTGrammarParser.MUL))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 183
                        self.expression(14)
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaASTGrammarParser.Expression1Context(self, MiniJavaASTGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 184
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 185
                        self.match(MiniJavaASTGrammarParser.LBRACK)
                        self.state = 186
                        self.expression(0)
                        self.state = 187
                        self.match(MiniJavaASTGrammarParser.RBRACK)
                        pass

                    elif la_ == 3:
                        localctx = MiniJavaASTGrammarParser.Expression2Context(self, MiniJavaASTGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 190
                        self.match(MiniJavaASTGrammarParser.DOT)
                        self.state = 191
                        self.match(MiniJavaASTGrammarParser.T__3)
                        pass

                    elif la_ == 4:
                        localctx = MiniJavaASTGrammarParser.Expression3Context(self, MiniJavaASTGrammarParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 193
                        self.match(MiniJavaASTGrammarParser.DOT)
                        self.state = 194
                        self.identifier()
                        self.state = 195
                        self.match(MiniJavaASTGrammarParser.LPAREN)
                        self.state = 204
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaASTGrammarParser.T__4) | (1 << MiniJavaASTGrammarParser.T__5) | (1 << MiniJavaASTGrammarParser.NEW) | (1 << MiniJavaASTGrammarParser.THIS) | (1 << MiniJavaASTGrammarParser.LPAREN) | (1 << MiniJavaASTGrammarParser.BANG) | (1 << MiniJavaASTGrammarParser.IDENTIFIER) | (1 << MiniJavaASTGrammarParser.INTEGER_LITERAL))) != 0):
                            self.state = 196
                            self.expression(0)
                            self.state = 201
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==MiniJavaASTGrammarParser.COMMA:
                                self.state = 197
                                self.match(MiniJavaASTGrammarParser.COMMA)
                                self.state = 198
                                self.expression(0)
                                self.state = 203
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 206
                        self.match(MiniJavaASTGrammarParser.RPAREN)
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.name_attr = str()

        def IDENTIFIER(self):
            return self.getToken(MiniJavaASTGrammarParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniJavaASTGrammarParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MiniJavaASTGrammarParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(MiniJavaASTGrammarParser.IDENTIFIER)
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
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         




