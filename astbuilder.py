from grammar.SnMsLangListener import SnMsLangListener

# Proste klasy AST

class ProgramNode:
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"ProgramNode(statements={self.statements})"  
class BlockNode:
    def __init__(self, statements):
        self.statements = statements


class AssignmentNode:
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr
    def __repr__(self):
        return f"AssignmentNode(var={self.var_name}, expr={repr(self.expr)})"    

class PrintNode:
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"PrintNode({repr(self.expr)})"     

class ReadNode:
    def __init__(self, var_name):
        self.var_name = var_name
    def __repr__(self):
        return f"ReadNode({self.var_name})"


class IfNode:
    def __init__(self, condition, then_block, else_block=None):
        self.condition = condition
        self.then_block = then_block
        self.else_block = else_block
    def __repr__(self):
        return f"IfNode(cond={self.condition}, then={self.then_block}, else={self.else_block})"

class BlockNode:
    def __init__(self, statements):
        self.statements = statements
    def __repr__(self):
        return f"BlockNode({self.statements})"



class BinaryOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinaryOpNode({repr(self.left)} {self.op} {repr(self.right)})"    

class IntNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"IntNode({self.value})"

class FloatNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"FloatNode({self.value})"


class VarNode:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"VarNode({self.name})"    

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __repr__(self):
        return f"WhileNode(cond={self.condition}, body={self.body})"



class ASTBuilder(SnMsLangListener):
    def __init__(self):
        self.stack = []

    def exitProgram(self, ctx):
        stmts = []
        while len(self.stack) > 0:
            stmts.insert(0, self.stack.pop())
        self.stack.append(ProgramNode(stmts))

    def exitBlock(self, ctx):
        stmts = []
        while isinstance(self.stack[-1], BlockNode):  # lub inna Twoja superklasa węzłów
            stmts.insert(0, self.stack.pop())
        self.stack.append(BlockNode(stmts))


    # np. x = 5 + 10;
    def exitAssignment(self, ctx):
        expr = self.stack.pop()
        var_name = ctx.ID().getText()
        self.stack.append(AssignmentNode(var_name, expr))

    # np. wypisz(x);
    def exitPrintStmt(self, ctx):
        expr = self.stack.pop()
        self.stack.append(PrintNode(expr))

    # np. 5 + 10
    def exitAddSubExpr(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(BinaryOpNode(left, op, right))

    # np. 5 * 10
    def exitMulDivExpr(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(BinaryOpNode(left, op, right))

    # liczba całkowita np. 5
    def exitIntExpr(self, ctx):
        value = int(ctx.INT().getText())
        self.stack.append(IntNode(value))

    def exitFloatExpr(self, ctx):
        value = float(ctx.FLOAT().getText())
        self.stack.append(FloatNode(value))


    def exitReadStmt(self, ctx):
        var_name = ctx.ID().getText()
        self.stack.append(ReadNode(var_name))

    def exitCompareExpr(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        op = ctx.getChild(1).getText()
        self.stack.append(BinaryOpNode(left, op, right))

    def exitBoolExpr(self, ctx):
        val = ctx.BOOL().getText()
        self.stack.append(IntNode(1 if val == "prawda" else 0))


    # zmienna np. x
    def exitIdExpr(self, ctx):
        var_name = ctx.ID().getText()
        self.stack.append(VarNode(var_name))

    def exitIfStmt(self, ctx):
        if ctx.getChildCount() == 5:
            # if (cond) thenBlock
            then_block = self.stack.pop()
            condition = self.stack.pop()
            self.stack.append(IfNode(condition, then_block))
        elif ctx.getChildCount() == 7:
            # if (cond) thenBlock else elseBlock
            else_block = self.stack.pop()
            then_block = self.stack.pop()
            condition = self.stack.pop()
            self.stack.append(IfNode(condition, then_block, else_block))

    def exitBlock(self, ctx):
        stmts = []
        while self.stack and isinstance(self.stack[-1], (AssignmentNode, PrintNode, ReadNode, IfNode)):
            stmts.insert(0, self.stack.pop())
        self.stack.append(BlockNode(stmts))


    def exitWhileStmt(self, ctx):
        body = self.stack.pop()
        condition = self.stack.pop()
        self.stack.append(WhileNode(condition, body))




    def get_ast(self):
        if len(self.stack) == 1:
            return self.stack[0]  # zwracaj bez listy
        return self.stack

def print_ast(node, indent=0):
    prefix = " " * (indent * 2)
    if isinstance(node, list):
        for n in node:
            print_ast(n, indent)
    elif isinstance(node, AssignmentNode):
        print(f"{prefix}AssignmentNode: var = {node.var_name}")
        print_ast(node.expr, indent + 1)
    elif isinstance(node, BinaryOpNode):
        print(f"{prefix}BinaryOpNode: op = {node.op}")
        print_ast(node.left, indent + 1)
        print_ast(node.right, indent + 1)
    elif isinstance(node, PrintNode):
        print(f"{prefix}PrintNode")
        print_ast(node.expr, indent + 1)
    elif isinstance(node, IntNode):
        print(f"{prefix}IntNode: {node.value}")
    elif isinstance(node, VarNode):
        print(f"{prefix}VarNode: {node.name}")
    elif isinstance(node, FloatNode):
        print(f"{prefix}FloatNode: {node.value}")    

