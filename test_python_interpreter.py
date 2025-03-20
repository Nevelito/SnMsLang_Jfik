from antlr4 import *
from grammar.SnMsLangLexer import SnMsLangLexer
from grammar.SnMsLangParser import SnMsLangParser
from grammar.SnMsLangListener import SnMsLangListener
from astbuilder import ProgramNode, AssignmentNode, PrintNode, BinaryOpNode, IntNode, VarNode, BlockNode, ASTBuilder, FloatNode, ReadNode

class Interpreter:
    def __init__(self):
        self.env = {}  # prosta "pamięć" na zmienne

    def run(self, ast):
        # obsłuż listę ProgramNode'ów
        if isinstance(ast, list):
            for node in ast:
                self.eval_node(node)
        else:
            self.eval_node(ast)

    def eval_node(self, node):
        if isinstance(node, ProgramNode):
            print(">> Eval: ProgramNode")
            for stmt in node.statements:
                self.eval_node(stmt)
        elif isinstance(node, AssignmentNode):
            val = self.eval_node(node.expr)
            self.env[node.var_name] = val
        elif isinstance(node, PrintNode):
            val = self.eval_node(node.expr)
            print("wypisz:", val)
        elif isinstance(node, ReadNode):
            user_input = input(f"Podaj wartość dla {node.var_name}: ")
            if '.' in user_input:
                value = float(user_input)
            else:
                value = int(user_input)
            self.env[node.var_name] = value
        elif isinstance(node, BinaryOpNode):
            left = self.eval_node(node.left)
            right = self.eval_node(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left // right
        elif isinstance(node, IntNode):
            return node.value
        elif isinstance(node, FloatNode):
            return node.value
        elif isinstance(node, VarNode):
            return self.env.get(node.name)
        else:
            print("DEBUG node type:", type(node))
            raise Exception(f"Nieznany węzeł AST: {node}")


    def dump_env(self):
        print("Środowisko zmiennych:", self.env)



if __name__ == "__main__":
    #input_stream = InputStream("x=5+15;wypisz(x);y=1;wypisz(x-y);")
    input_stream = InputStream("pi = 0.0;wczytaj(pi);wypisz(pi);")

    lexer = SnMsLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SnMsLangParser(tokens)
    tree = parser.program()


    builder = ASTBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)

    ast = builder.get_ast()
    print(ast)
    interpreter = Interpreter()
    interpreter.run(ast)
    interpreter.dump_env()
 