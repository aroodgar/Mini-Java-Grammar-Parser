from gen.MiniJavaASTGrammarListener import MiniJavaASTGrammarListener
from gen.MiniJavaASTGrammarParser import MiniJavaASTGrammarParser
from gen.MiniJavaASTGrammarLexer import MiniJavaASTGrammarLexer
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
from antlr4 import *


class ASTListener(MiniJavaASTGrammarListener):
    def __init__(self):
        self.ast = AST()
        self.backtrack_queue = []

    def get_ast_root(self):
        return self.ast.root

    def exitProgram(self, ctx: MiniJavaASTGrammarParser.ProgramContext):
        ctx.name_attr = 'program'
        child_count = ctx.getChildCount() - 1
        class_declaration_ptr_list = []
        ctx.value_attr = str(ctx.mainClass().value_attr)
        for i in range(child_count - 1):
            class_declaration_ptr_list.append(self.backtrack_queue.pop())
            ctx.value_attr += ' ' + str(ctx.classDeclaration(i).value_attr)
        main_class_ptr = self.backtrack_queue.pop()
        program_ptr = self.ast.make_node(value=ctx.value_attr, child=main_class_ptr, brother=None, name=ctx.name_attr)
        class_declaration_ptr_list = class_declaration_ptr_list[::-1]
        self.ast.add_brother(node=main_class_ptr, new_brother=class_declaration_ptr_list[0])
        for i in range(1, len(class_declaration_ptr_list)):
            self.ast.add_brother(node=class_declaration_ptr_list[i - 1], new_brother=class_declaration_ptr_list[i])
        self.backtrack_queue.append(program_ptr)
        self.ast.root = program_ptr

    def exitMainClass(self, ctx: MiniJavaASTGrammarParser.MainClassContext):
        ctx.name_attr = 'mainClass'
        ctx.value_attr = f'class {str(ctx.identifier(0).value_attr)} ' \
                         f'{str(ctx.LBRACE())} public void main (String[] {str(ctx.identifier(1).value_attr)})' \
                         f'{str(ctx.LBRACE())} {str(ctx.statement().value_attr)} {str(ctx.RBRACE())} {str(ctx.RBRACE())}'
        st_ptr = self.backtrack_queue.pop()
        identifier_param_ptr = self.backtrack_queue.pop()
        identifier_class_ptr = self.backtrack_queue.pop()
        main_class_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=identifier_class_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=identifier_class_ptr, new_brother=identifier_param_ptr)
        self.ast.add_brother(node=identifier_param_ptr, new_brother=st_ptr)
        self.backtrack_queue.append(main_class_ptr)

    def exitClassDeclaration(self, ctx: MiniJavaASTGrammarParser.ClassDeclarationContext):
        ctx.name_attr = 'classDeclaration'
        child_count = ctx.getChildCount()
        var_method_declaration_ptr_list = []
        identifier_extends_ptr = None
        if ctx.EXTENDS() is not None:
            if child_count > 6:
                for _ in range(child_count - 6):
                    var_method_declaration_ptr_list.append(self.backtrack_queue.pop())
            identifier_extends_ptr = self.backtrack_queue.pop()
        else:
            if child_count > 4:
                for _ in range(child_count - 4):
                    var_method_declaration_ptr_list.append(self.backtrack_queue.pop())
        identifier_class_ptr = self.backtrack_queue.pop()
        ctx.value_attr = ctx.identifier(0).value_attr
        if identifier_extends_ptr is not None:
            ctx.value_attr += ctx.identifier(1).value_attr
            self.ast.add_brother(node=identifier_class_ptr, new_brother=identifier_extends_ptr)
        class_declaration_ptr = \
            self.ast.make_node(value=ctx.value_attr, child=identifier_class_ptr, brother=None, name=ctx.name_attr)
        var_method_declaration_ptr_list = var_method_declaration_ptr_list[::-1]
        if identifier_extends_ptr is not None:
            if len(var_method_declaration_ptr_list) > 0:
                self.ast.add_brother(node=identifier_extends_ptr, new_brother=var_method_declaration_ptr_list[0])
        else:
            if len(var_method_declaration_ptr_list) > 0:
                self.ast.add_brother(node=identifier_class_ptr, new_brother=var_method_declaration_ptr_list[0])
        for i in range(1, len(var_method_declaration_ptr_list)):
            self.ast.add_brother(node=var_method_declaration_ptr_list[i - 1],
                                 new_brother=var_method_declaration_ptr_list[i])
        self.backtrack_queue.append(class_declaration_ptr)

    def exitMethodDeclaration(self, ctx: MiniJavaASTGrammarParser.MethodDeclarationContext):
        ctx.name_attr = 'methodDeclaration'
        comma_type_id_ptr_list = []
        expr_ptr = self.backtrack_queue.pop()
        index = 0
        var_st_ptr_list = []
        while ctx.statement(index) is not None:
            var_st_ptr_list.append(self.backtrack_queue.pop())
            index += 1
        index = 0
        while ctx.varDeclaration(index) is not None:
            var_st_ptr_list.append(self.backtrack_queue.pop())
            index += 1
        var_st_ptr_list = var_st_ptr_list[::-1]
        id_question_mark_ptr = None
        type_question_mark_ptr = None
        if ctx.identifier(1) is not None:
            index = 0
            while ctx.COMMA(index) is not None:
                comma_type_id_ptr_list.append(self.backtrack_queue.pop())
                comma_type_id_ptr_list.append(self.backtrack_queue.pop())
                index += 1
            id_question_mark_ptr = self.backtrack_queue.pop()
            type_question_mark_ptr = self.backtrack_queue.pop()
        comma_type_id_ptr_list = comma_type_id_ptr_list[::-1]
        id_public_ptr = self.backtrack_queue.pop()
        type_public_ptr = self.backtrack_queue.pop()
        ctx.value_attr = ctx.type(0).value_attr + ctx.identifier(0).value_attr + '('
        if type_question_mark_ptr is not None:
            ctx.value_attr += ctx.type(1).value_attr + ctx.identifier(1).value_attr
            for i in range(len(comma_type_id_ptr_list)):
                ind = int(i / 2)
                print(ctx.type(ind + 2) is None, ind + 2, len(comma_type_id_ptr_list))
                print(ctx.identifier(ind + 2) is None, ind + 2, len(comma_type_id_ptr_list))
                ctx.value_attr += ',' + ctx.type(ind + 2).value_attr + ctx.identifier(ind + 2).value_attr
        else:
            ctx.value_attr += ctx.type(1).value_attr + ctx.identifier(1)
            for i in range(len(comma_type_id_ptr_list) - 1):
                ind = int(i / 2)
                ctx.value_attr += ',' + ctx.type(ind + 2).value_attr + ctx.identifier(ind + 2).value_attr
        ctx.value_attr += ')'

        method_declaration_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=type_public_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=type_public_ptr, new_brother=id_public_ptr)
        if type_question_mark_ptr is not None:
            self.ast.add_brother(node=id_public_ptr, new_brother=type_question_mark_ptr)
            self.ast.add_brother(node=type_question_mark_ptr, new_brother=id_question_mark_ptr)
            if len(comma_type_id_ptr_list) > 0:
                self.ast.add_brother(node=id_question_mark_ptr, new_brother=comma_type_id_ptr_list[0])
                if len(var_st_ptr_list) > 0:
                    self.ast.add_brother(node=comma_type_id_ptr_list[len(comma_type_id_ptr_list) - 1],
                                         new_brother=var_st_ptr_list[0])
                else:
                    self.ast.add_brother(node=comma_type_id_ptr_list[len(comma_type_id_ptr_list) - 1],
                                         new_brother=expr_ptr)
            else:
                if len(var_st_ptr_list) > 0:
                    self.ast.add_brother(node=id_question_mark_ptr, new_brother=var_st_ptr_list[0])
                else:
                    self.ast.add_brother(node=id_question_mark_ptr, new_brother=expr_ptr)
        else:
            if len(var_st_ptr_list) > 0:
                self.ast.add_brother(node=id_public_ptr, new_brother=var_st_ptr_list[0])
            else:
                self.ast.add_brother(node=id_public_ptr, new_brother=expr_ptr)
        for i in range(1, len(comma_type_id_ptr_list)):
            self.ast.add_brother(node=comma_type_id_ptr_list[i - 1], new_brother=comma_type_id_ptr_list[i])
        for i in range(1, len(var_st_ptr_list)):
            self.ast.add_brother(node=var_st_ptr_list[i - 1], new_brother=var_st_ptr_list[i])
        self.backtrack_queue.append(method_declaration_ptr)

    def exitVarDeclaration(self, ctx: MiniJavaASTGrammarParser.VarDeclarationContext):
        ctx.name_attr = 'varDeclaration'
        ctx.value_attr = ctx.type().value_attr + ' Var Type Declaration'
        identifier_ptr = self.backtrack_queue.pop()
        type_ptr = self.backtrack_queue.pop()
        var_declaration_ptr = self.ast.make_node(value=ctx.value_attr, child=type_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=type_ptr, new_brother=identifier_ptr)
        self.backtrack_queue.append(var_declaration_ptr)

    def exitType0(self, ctx: MiniJavaASTGrammarParser.Type0Context):
        ctx.name_attr = 'type0'
        ctx.value_attr = str(ctx.INT()) + str(ctx.LBRACK()) + str(ctx.RBRACK())
        type0_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(type0_ptr)

    def exitType1(self, ctx: MiniJavaASTGrammarParser.Type1Context):
        ctx.name_attr = 'type1'
        ctx.value_attr = str(ctx.BOOLEAN())
        type1_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(type1_ptr)

    def exitType2(self, ctx: MiniJavaASTGrammarParser.Type2Context):
        ctx.name_attr = 'type2'
        ctx.value_attr = str(ctx.INT())
        type2_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(type2_ptr)

    def exitStatement0(self, ctx: MiniJavaASTGrammarParser.Statement0Context):
        ctx.name_attr = 'statement0'
        child_count = ctx.getChildCount() - 2
        ctx.value_attr = ''
        for i in range(child_count - 1):
            ctx.value_attr += ctx.statement(i).value_attr + ' '
        ctx.value_attr += ctx.statement(child_count - 1).value_attr

        children_nodes = []
        for _ in range(child_count):
            children_nodes.append(self.backtrack_queue.pop())
        statement0_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=children_nodes[0], brother=None, name=ctx.name_attr)
        for i in range(1, len(children_nodes)):
            self.ast.add_brother(node=children_nodes[i - 1], new_brother=children_nodes[i])
        self.backtrack_queue.append(statement0_ptr)

    def exitStatement1(self, ctx: MiniJavaASTGrammarParser.Statement1Context):
        ctx.name_attr = 'statement1'
        ctx.value_attr = str(ctx.IF()) + str(ctx.LPAREN()) + ctx.expression().value_attr + str(ctx.RPAREN())\
                         + ctx.statement(0).value_attr + str(ctx.ELSE()) + ctx.statement(1).value_attr
        st_right_ptr = self.backtrack_queue.pop()
        st_left_ptr = self.backtrack_queue.pop()
        expr_ptr = self.backtrack_queue.pop()
        statement1_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=expr_ptr, new_brother=st_left_ptr)
        self.ast.add_brother(node=st_left_ptr, new_brother=st_right_ptr)
        self.backtrack_queue.append(statement1_ptr)

    def exitStatement2(self, ctx: MiniJavaASTGrammarParser.Statement2Context):
        ctx.name_attr = 'statement2'
        ctx.value_attr = \
            str(ctx.WHILE()) + str(ctx.LPAREN()) + ctx.expression().value_attr + str(ctx.RPAREN())\
            + ctx.statement().value_attr
        st_ptr = self.backtrack_queue.pop()
        expr_ptr = self.backtrack_queue.pop()
        statement2_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=expr_ptr, new_brother=st_ptr)
        self.backtrack_queue.append(statement2_ptr)

    def exitStatement3(self, ctx: MiniJavaASTGrammarParser.Statement3Context):
        ctx.name_attr = 'statement3'
        ctx.value_attr = 'System.out.println' + str(ctx.LPAREN()) + ctx.expression().value_attr + str(ctx.RPAREN())
        expr_ptr = self.backtrack_queue.pop()
        statement3_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(statement3_ptr)

    def exitStatement4(self, ctx: MiniJavaASTGrammarParser.Statement4Context):
        ctx.name_attr = 'statement4'
        ctx.value_attr = str(ctx.ASSIGN())
        expr_ptr = self.backtrack_queue.pop()
        identifier_ptr = self.backtrack_queue.pop()
        statement4_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=identifier_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=identifier_ptr, new_brother=expr_ptr)
        self.backtrack_queue.append(statement4_ptr)

    def exitStatement5(self, ctx: MiniJavaASTGrammarParser.Statement5Context):
        ctx.name_attr = 'statement5'
        ctx.value_attr = str(ctx.LBRACK) + str(ctx.RBRACK) + str(ctx.ASSIGN())
        expr_right_ptr = self.backtrack_queue.pop()
        expr_index_ptr = self.backtrack_queue.pop()
        st_ptr = self.backtrack_queue.pop()
        statement5_ptr = self.ast.make_node(value=ctx.value_attr, child=st_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=st_ptr, new_brother=expr_index_ptr)
        self.ast.add_brother(node=expr_index_ptr, new_brother=expr_right_ptr)
        self.backtrack_queue.append(statement5_ptr)

    def exitExpression0(self, ctx: MiniJavaASTGrammarParser.Expression0Context):
        ctx.name_attr = 'expression0'
        expr_right_ptr = self.backtrack_queue.pop()
        expr_left_ptr = self.backtrack_queue.pop()
        if ctx.AND() is not None:
            operator = ctx.AND()
        elif ctx.LT() is not None:
            operator = ctx.LT()
        elif ctx.ADD() is not None:
            operator = ctx.ADD()
        elif ctx.SUB() is not None:
            operator = ctx.SUB()
        else:
            operator = ctx.MUL()
        ctx.value_attr = ctx.expression(0).value_attr + str(operator) + ctx.expression(1).value_attr
        expression0_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=expr_left_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=expr_left_ptr, new_brother=expr_right_ptr)
        self.backtrack_queue.append(expression0_ptr)

    def exitExpression1(self, ctx: MiniJavaASTGrammarParser.Expression1Context):
        ctx.name_attr = 'expression1'
        expr_right_ptr = self.backtrack_queue.pop()
        expr_left_ptr = self.backtrack_queue.pop()
        ctx.value_attr = \
            ctx.expression(0).value_attr + str(ctx.LBRACK()) + ctx.expression(1).value_attr + str(ctx.RBRACK())
        expression1_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=expr_left_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=expr_left_ptr, new_brother=expr_right_ptr)
        self.backtrack_queue.append(expression1_ptr)

    def exitExpression2(self, ctx: MiniJavaASTGrammarParser.Expression2Context):
        ctx.name_attr = 'expression2'
        expr_ptr = self.backtrack_queue.pop()
        ctx.value_attr = ctx.expression().value_attr + str(ctx.DOT()) + 'length'
        expression2_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression2_ptr)

    def exitExpression3(self, ctx: MiniJavaASTGrammarParser.Expression3Context):
        ctx.name_attr = 'expression3'
        child_count = ctx.getChildCount()
        children_nodes = []
        tmp_child_count = child_count
        if child_count > 6:
            tmp_child_count = int((child_count - 6) / 2)
            tmp_child_count += 3
        else:
            tmp_child_count -= 3

        for _ in range(tmp_child_count):
            children_nodes.append(self.backtrack_queue.pop())
        expr_star_ptr_list = None
        expr_question_mark_ptr = None
        if tmp_child_count > 2:
            if tmp_child_count > 3:
                expr_star_ptr_list = children_nodes[3:]
            expr_question_mark_ptr = children_nodes[2]
        identifier_ptr = children_nodes[1]
        expr_default_ptr = children_nodes[0]
        ctx.value_attr = ctx.expression(0).value_attr + str(ctx.DOT()) + ctx.identifier().value_attr
        expression3_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=expr_default_ptr, brother=None, name=ctx.name_attr)
        self.ast.add_brother(node=expr_default_ptr, new_brother=identifier_ptr)
        if expr_question_mark_ptr is not None:
            self.ast.add_brother(node=identifier_ptr, new_brother=expr_question_mark_ptr)
            if expr_star_ptr_list is not None:
                self.ast.add_brother(node=expr_question_mark_ptr, new_brother=expr_star_ptr_list[0])
                for i in range(1, len(expr_star_ptr_list)):
                    self.ast.add_brother(node=expr_star_ptr_list[i - 1], new_brother=expr_star_ptr_list[i])
        self.backtrack_queue.append(expression3_ptr)

    def exitExpression4(self, ctx: MiniJavaASTGrammarParser.Expression4Context):
        ctx.name_attr = 'expression4'
        ctx.value_attr = str(ctx.INTEGER_LITERAL())
        int_literal_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(int_literal_ptr)

    def exitExpression5(self, ctx: MiniJavaASTGrammarParser.Expression5Context):
        ctx.name_attr = 'expression5'
        ctx.value_attr = 'true'
        true_ptr = self.ast.make_node(value='true', child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(true_ptr)

    def exitExpression6(self, ctx: MiniJavaASTGrammarParser.Expression6Context):
        ctx.name_attr = 'expression6'
        ctx.value_attr = 'false'
        false_ptr = self.ast.make_node(value='false', child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(false_ptr)

    def exitExpression7(self, ctx: MiniJavaASTGrammarParser.Expression7Context):
        ctx.name_attr = 'expression7'
        ctx.value_attr = ctx.identifier().value_attr
        identifier_ptr = self.backtrack_queue.pop()
        expression7 = self.ast.make_node(value=ctx.value_attr, child=identifier_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression7)

    def exitExpression8(self, ctx: MiniJavaASTGrammarParser.Expression8Context):
        ctx.name_attr = 'expression8'
        ctx.value_attr = str(ctx.THIS())
        this_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(this_ptr)

    def exitExpression9(self, ctx: MiniJavaASTGrammarParser.Expression9Context):
        ctx.name_attr = 'expression9'
        ctx.value_attr = ctx.expression().value_attr
        expr_ptr = self.backtrack_queue.pop()
        expression9_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression9_ptr)

    def exitExpression10(self, ctx: MiniJavaASTGrammarParser.Expression10Context):
        ctx.name_attr = 'expression10'
        ctx.value_attr = ctx.identifier().value_attr
        identifier_ptr = self.backtrack_queue.pop()
        expression10_ptr = self.ast.make_node\
            (value=ctx.value_attr, child=identifier_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression10_ptr)

    def exitExpression11(self, ctx: MiniJavaASTGrammarParser.Expression11Context):
        ctx.name_attr = 'expression11'
        ctx.value_attr = ctx.expression().value_attr
        expr_ptr = self.backtrack_queue.pop()
        expression11_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression11_ptr)

    def exitExpression12(self, ctx: MiniJavaASTGrammarParser.Expression12Context):
        ctx.name_attr = 'expression12'
        ctx.value_attr = ctx.expression().value_attr
        expr_ptr = self.backtrack_queue.pop()
        expression12_ptr = self.ast.make_node(value=ctx.value_attr, child=expr_ptr, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(expression12_ptr)

    def exitIdentifier(self, ctx: MiniJavaASTGrammarParser.IdentifierContext):
        ctx.name_attr = 'identifier'
        ctx.value_attr = str(ctx.IDENTIFIER())
        identifier_ptr = self.ast.make_node(value=ctx.value_attr, child=None, brother=None, name=ctx.name_attr)
        self.backtrack_queue.append(identifier_ptr)


class ASTGenerator:
    def __init__(self, ast_root):
        self.ast = ast_root
        self.remove_additional_nodes(self.ast)

    def remove_additional_nodes(self, ast):
        if ast.brother is None:
            if ast.child is not None:
                new_node = self.remove_additional_nodes(ast.child)
                if ast.parent is not None:
                    AST.change_child(ast.parent, new_node)
                    AST.set_parent(new_node, ast.parent)
                return new_node
            else:
                return ast
        else:
            new_brother = self.remove_additional_nodes(ast.brother)
            if ast.child is not None:
                new_node = self.remove_additional_nodes(ast.child)
                if new_node.brother is None:
                    if ast.parent is not None:
                        AST.change_child(ast.parent, new_node)
                        AST.set_parent(new_node, ast.parent)
                    elif ast.older_brother is not None:
                        AST.change_brother(ast.older_brother, new_node)
                        AST.set_older_brother(new_node, ast.older_brother)
                    AST.change_brother(new_node, new_brother)
                    AST.set_older_brother(new_brother, new_node)
                    return new_node
                else:
                    AST.change_child(ast, new_node)
                    AST.set_parent(new_node, ast)
            AST.change_brother(ast, new_brother)
            AST.set_older_brother(new_brother, ast)
            return ast

    def get_ast(self):
        return self.ast


class Graph:
    def __init__(self, ast_root):
        self.g = nx.DiGraph()
        self.labels = {}
        self.counter = 0
        self.edge_list = []
        self.node_list = []
        self.graph_labels = {}
        self.node_colors = {0: 'blue'}
        self.create_directed_graph_from_ast(ast_root)
        self.create_nx_graph(self.edge_list, self.node_list)
        print([e for e in self.g.edges])
        for el in list(self.g.nodes(data=True)):
            print(el)

    def create_nx_graph(self, edge_list, node_list):
        self.g.add_nodes_from(node_list)
        for e in edge_list:
            self.g.add_edge(e[0], e[1], color=e[2])

    def create_directed_graph_from_ast(self, ast, is_child=False):
        brother = None
        child = None
        self.node_list.append((self.counter, {'ptr': ast, 'value': ast.value, '_name': ast.name}))
        self.labels[ast] = (self.counter, ast.value)
        id_count = self.counter
        self.counter += 1
        if ast.brother is not None:
            brother_id, brother = self.create_directed_graph_from_ast(ast.brother)
        if ast.child is not None:
            child_id, child = self.create_directed_graph_from_ast(ast.child, True)
            self.graph_labels[id_count] = ast.name + '(c)' if is_child else ast.name
            ast.label = self.graph_labels[id_count]
        else:
            self.graph_labels[id_count] = ast.value + '(c)' if is_child else ast.value
            ast.label = self.graph_labels[id_count]
        if brother is not None:
            self.labels[ast.brother] = (self.counter, ast.brother.value)
            self.node_colors[self.counter] = 'blue'
            self.edge_list.append((self.labels[ast][0], brother_id, 'b'))
        if child is not None:
            self.labels[ast.child] = (self.counter, ast.child.value)
            self.node_colors[self.counter] = 'lightgreen'
            self.edge_list.append((self.labels[ast][0], child_id, 'g'))
        return [id_count, ast]

    def draw_graph(self):
        # plt.subplot(111)
        colors = nx.get_edge_attributes(self.g, 'color').values()
        pos = graphviz_layout(self.g, prog='dot', root=0)
        nx.draw_networkx(self.g, with_labels=True, pos=pos, labels=self.graph_labels, edge_color=colors)
        plt.show()


class TreeNode:
    def __init__(self, value, child, brother, name):
        self.name = name
        self.value = value
        self.child = child
        self.brother = brother
        self.older_brother = None
        self.parent = None
        self.label = None


class ThreeAddressCode:
    def __init__(self, ast_root):
        self.ast = ast_root
        self.instruction_list = []
        self.op_dict = {'program': 'program',
                        'mainClass': 'mnCls',
                        'classDeclaration': 'clsDec',
                        'methodDeclaration': 'mtdDec',
                        'varDeclaration': 'varDec',
                        'type0': 'tp0',
                        'type1': 'tp1',
                        'type2': 'tp2',
                        'statement0': 'st0',
                        'statement1': 'st1',
                        'statement2': 'st2',
                        'statement3': 'st3',
                        'statement4': 'st4',
                        'statement5': 'st5',
                        'expression0': 'e0',
                        'expression1': 'e1',
                        'expression2': 'e2',
                        'expression3': 'e3',
                        'expression4': 'e4',
                        'expression5': 'e5',
                        'expression6': 'e6',
                        'expression7': 'e7',
                        'expression8': 'e8',
                        'expression9': 'e9',
                        'expression10': 'e10',
                        'expression11': 'e11',
                        'expression12': 'e12',
                        'identifier': 'id'}
        self.traverse_and_create_instructions(self.ast)

    def traverse_and_create_instructions(self, node):
        child_label = ''
        brother_label = ''
        if node.child is not None:
            child_label = self.traverse_and_create_instructions(node.child)
        if node.brother is not None:
            brother_label = self.traverse_and_create_instructions(node.brother)
        node_label = self.op_dict[node.name]
        if node.child is None and node.brother is None:
            operands_str = node.value
        elif node.child is None:
            operands_str = brother_label
        elif node.brother is None:
            operands_str = child_label
        else:
            operands_str = ', '.join([child_label, brother_label])
        self.instruction_list.append(' '.join([node_label, operands_str]))
        return node_label

    def get_instructions(self):
        return self.instruction_list


class AST:
    def __init__(self):
        self.root = None
        self.current = None

    def make_node(self, value, child, brother, name):
        tree_node = TreeNode(value, child, brother, name)
        if child is not None:
            self.set_parent(child, tree_node)
        self.current = tree_node
        return tree_node

    def add_child(self, node, new_child):
        if node.child is None:
            node.child = new_child
        else:
            self.current = node.child
            while self.current.child is not None:
                self.current = self.current.child
            self.current.child = new_child
        self.current = new_child

    def add_brother(self, node, new_brother):
        if node.brother is None:
            node.brother = new_brother
            self.set_older_brother(new_brother, node)
        else:
            self.current = node.brother
            while self.current.brother is not None:
                self.current = self.current.brother
            self.current.brother = new_brother
            self.set_older_brother(new_brother, self.current)
        self.current = new_brother

    @staticmethod
    def set_parent(node, parent):
        node.parent = parent

    @staticmethod
    def set_older_brother(node, older_brother):
        node.older_brother = older_brother

    @staticmethod
    def change_brother(node, new_brother):
        node.brother = new_brother

    @staticmethod
    def change_child(node, new_child):
        node.child = new_child


def main():
    address = input()
    listener = ASTListener()
    fs = FileStream(address)
    lexer = MiniJavaASTGrammarLexer(fs)
    token_stream = CommonTokenStream(lexer)
    parser = MiniJavaASTGrammarParser(token_stream)
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    ast_root = listener.get_ast_root()
    ast_generator = ASTGenerator(ast_root)
    ast_root = ast_generator.get_ast()
    graph = Graph(ast_root)
    graph.draw_graph()
    three_address_code_obj = ThreeAddressCode(ast_root)
    instructions = three_address_code_obj.get_instructions()
    print('*** (Instructions) ***')
    for instruction in instructions:
        print(instruction)


if __name__ == '__main__':
    main()
