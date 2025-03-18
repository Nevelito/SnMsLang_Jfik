import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grammar.SnMsLangLexer import SnMsLangLexer
from grammar.SnMsLangParser import SnMsLangParser
from grammar.SnMsLangListener import SnMsLangListener
from antlr4 import *

class VariableNode:
    def __init__(self, name, var_type='int'):
        self.name = name
        self.type = var_type

class ArithmeticOperationNode:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

class PrintNode:
    def __init__(self, expression):
        self.expression = expression

class ASTBuilder(SnMsLangListener):
    def __init__(self):
        self.ast = []

    def exitVariable(self, ctx):
        var_name = ctx.ID().getText()
        self.ast.append(VariableNode(var_name))

    def exitArithmeticExpression(self, ctx):
        left = self.ast.pop()
        right = self.ast.pop()
        operator = ctx.OP().getText()
        self.ast.append(ArithmeticOperationNode(left, right, operator))

    def exitPrintStatement(self, ctx):
        expr = self.ast.pop()
        self.ast.append(PrintNode(expr))

    def get_ast(self):
        return self.ast

def parse_code(code):
    input_stream = InputStream(code)
    lexer = SnMsLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SnMsLangParser(stream)
    tree = parser.program()

    builder = ASTBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)

    return builder.get_ast()
