from antlr4 import *
from grammar.SnMsLangLexer import SnMsLangLexer
from grammar.SnMsLangParser import SnMsLangParser
from grammar.SnMsLangListener import SnMsLangListener
from astbuilder import *

#input_stream = InputStream("x=5+15;wypisz(x);y=1;wypisz(x-y);")
input_stream = InputStream("x=0; dopoki(x<3){ x=x+1;wypisz(x);  }")

lexer = SnMsLangLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = SnMsLangParser(tokens)
tree = parser.program()


builder = ASTBuilder()
walker = ParseTreeWalker()
walker.walk(builder, tree)

ast = builder.get_ast()

print(ast)

print_ast(ast)