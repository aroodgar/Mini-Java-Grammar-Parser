# Mini-Java-Grammar-Parser
Mini Java Grammar Parser and AST Generator implemented in python using ANTLR API

## Mini Java Grammar Link which this project is based on:
http://www.cs.tufts.edu/~sguyer/classes/comp181-2006/minijava.html

## grammars directory
Includes two grammar files, one leverages attributes which is used in the actual code to help us keep more detailed info about each parsed node.

## ASTGenerator.py
Consists of a class ASTListener which is responsible for parsing the tree of a given MiniJavaGrammar-compliant code and building child and brother relationships needed for an AST.
The class ASTGenerator is responsible to convert the given parse tree with child-brother info to a binary tree which is the essence of an AST.
Finally, the ThreeAddressCode is a class which does somewhat of a mimic of an actual 3-address code generation procedure given the AST.
