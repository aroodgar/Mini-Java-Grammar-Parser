# Generated from F:/IUST_4001/Compiler/HW4/Practical/grammars\MiniJavaASTGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaASTGrammarParser import MiniJavaASTGrammarParser
else:
    from MiniJavaASTGrammarParser import MiniJavaASTGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaASTGrammarParser.

class MiniJavaASTGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaASTGrammarParser#program.
    def visitProgram(self, ctx:MiniJavaASTGrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#mainClass.
    def visitMainClass(self, ctx:MiniJavaASTGrammarParser.MainClassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaASTGrammarParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaASTGrammarParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaASTGrammarParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#type0.
    def visitType0(self, ctx:MiniJavaASTGrammarParser.Type0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#type1.
    def visitType1(self, ctx:MiniJavaASTGrammarParser.Type1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#type2.
    def visitType2(self, ctx:MiniJavaASTGrammarParser.Type2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement0.
    def visitStatement0(self, ctx:MiniJavaASTGrammarParser.Statement0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement1.
    def visitStatement1(self, ctx:MiniJavaASTGrammarParser.Statement1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement2.
    def visitStatement2(self, ctx:MiniJavaASTGrammarParser.Statement2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement3.
    def visitStatement3(self, ctx:MiniJavaASTGrammarParser.Statement3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement4.
    def visitStatement4(self, ctx:MiniJavaASTGrammarParser.Statement4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#statement5.
    def visitStatement5(self, ctx:MiniJavaASTGrammarParser.Statement5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression6.
    def visitExpression6(self, ctx:MiniJavaASTGrammarParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression7.
    def visitExpression7(self, ctx:MiniJavaASTGrammarParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression4.
    def visitExpression4(self, ctx:MiniJavaASTGrammarParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression5.
    def visitExpression5(self, ctx:MiniJavaASTGrammarParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression2.
    def visitExpression2(self, ctx:MiniJavaASTGrammarParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression3.
    def visitExpression3(self, ctx:MiniJavaASTGrammarParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression0.
    def visitExpression0(self, ctx:MiniJavaASTGrammarParser.Expression0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression1.
    def visitExpression1(self, ctx:MiniJavaASTGrammarParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression8.
    def visitExpression8(self, ctx:MiniJavaASTGrammarParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression10.
    def visitExpression10(self, ctx:MiniJavaASTGrammarParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression9.
    def visitExpression9(self, ctx:MiniJavaASTGrammarParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression12.
    def visitExpression12(self, ctx:MiniJavaASTGrammarParser.Expression12Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#expression11.
    def visitExpression11(self, ctx:MiniJavaASTGrammarParser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaASTGrammarParser#identifier.
    def visitIdentifier(self, ctx:MiniJavaASTGrammarParser.IdentifierContext):
        return self.visitChildren(ctx)



del MiniJavaASTGrammarParser