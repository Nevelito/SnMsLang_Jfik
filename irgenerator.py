from llvmlite import ir
import llvmlite.binding as llvm

from antlr4 import *
from grammar.SnMsLangLexer import SnMsLangLexer
from grammar.SnMsLangParser import SnMsLangParser
from astbuilder import *
from errorchecker import CustomErrorListener


class IRGenerator:
    def __init__(self):
        self.module = ir.Module(name="program")
        self.builder = None
        self.func_main = None
        self.fmt = None  # tutaj zrobimy globalny format dla printf

        # Dodajemy poprawny target triple
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()
        target = llvm.Target.from_default_triple()
        triple = target.triple
        self.module.triple = triple
        self.symbols = {}  # mapa zmiennych

    def generate(self, ast):
        # Zaczynamy od wygenerowania "main"
        func_type = ir.FunctionType(ir.VoidType(), [])
        self.func_main = ir.Function(self.module, func_type, name="main")
        block = self.func_main.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        if isinstance(ast, ProgramNode):
            for stmt in ast.statements:
                self.gen_stmt(stmt)

        self.builder.ret_void()
        return str(self.module)
    

    def get_or_create_fmt(self, fmt_str):
        if fmt_str not in self.symbols:
            fmt_type = ir.ArrayType(ir.IntType(8), len(fmt_str) + 1)
            fmt = ir.GlobalVariable(self.module, fmt_type, name=f"fmt_{len(self.symbols)}")
            fmt.linkage = 'internal'
            fmt.global_constant = True
            fmt.initializer = ir.Constant(fmt_type, bytearray((fmt_str + '\0').encode("utf8")))
            self.symbols[fmt_str] = fmt
        return self.symbols[fmt_str]




    def gen_stmt(self, node):
        if isinstance(node, AssignmentNode):
            val = self.gen_expr(node.expr)
            
            # Sprawdź typ wyrażenia i utwórz odpowiednie alloca
            if node.var_name not in self.symbols:
                if val.type == ir.IntType(32):
                    ptr = self.builder.alloca(ir.IntType(32), name=node.var_name)
                elif val.type == ir.DoubleType():
                    ptr = self.builder.alloca(ir.DoubleType(), name=node.var_name)
                self.symbols[node.var_name] = ptr
            else:
                ptr = self.symbols[node.var_name]

            self.builder.store(val, ptr)
        elif isinstance(node, PrintNode):
            val = self.gen_expr(node.expr)
            self.gen_print(val)
        elif isinstance(node, ReadNode):
            ptr = self.symbols.get(node.var_name)
            if ptr is None:
                # Jeśli zmienna jeszcze nie istnieje, załóż domyślnie jako i32
                ptr = self.builder.alloca(ir.IntType(32), name=node.var_name)
                self.symbols[node.var_name] = ptr
            self.gen_read(ptr)
        elif isinstance(node, IfNode):
            cond_val = self.gen_expr(node.condition)
            cond_bool = self.builder.icmp_signed('!=', cond_val, ir.Constant(cond_val.type, 0))

            then_bb = self.func_main.append_basic_block(name="then")
            else_bb = self.func_main.append_basic_block(name="else") if node.else_block else None
            end_bb = self.func_main.append_basic_block(name="endif")

            if else_bb:
                self.builder.cbranch(cond_bool, then_bb, else_bb)
            else:
                self.builder.cbranch(cond_bool, then_bb, end_bb)

            # THEN block
            self.builder.position_at_start(then_bb)
            for stmt in node.then_block.statements:
                self.gen_stmt(stmt)
            if not self.builder.block.is_terminated:
                self.builder.branch(end_bb)

            # ELSE block
            if else_bb:
                self.builder.position_at_start(else_bb)
                for stmt in node.else_block.statements:
                    self.gen_stmt(stmt)
                if not self.builder.block.is_terminated:
                    self.builder.branch(end_bb)

            # END block
            self.builder.position_at_start(end_bb)
                    


    def gen_read(self, ptr):
        val_type = ptr.type.pointee

        if val_type == ir.IntType(32):
            fmt = self.get_or_create_fmt("%d")
        elif val_type == ir.DoubleType():
            fmt = self.get_or_create_fmt("%lf")

        zero = ir.Constant(ir.IntType(32), 0)
        fmt_ptr = self.builder.gep(fmt, [zero, zero])

        # @scanf deklaracja
        scanf = self.module.globals.get('scanf')
        if scanf is None:
            scanf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            scanf = ir.Function(self.module, scanf_ty, name="scanf")

        self.builder.call(scanf, [fmt_ptr, ptr])



    def gen_expr(self, node):
        if isinstance(node, IntNode):
            return ir.Constant(ir.IntType(32), node.value)
        elif isinstance(node, FloatNode):
            return ir.Constant(ir.DoubleType(), node.value)
        elif isinstance(node, VarNode):
            ptr = self.symbols[node.name]
            return self.builder.load(ptr)
        elif isinstance(node, BinaryOpNode):
            left = self.gen_expr(node.left)
            right = self.gen_expr(node.right)

            # Sprawdź typ operandu
            if left.type == ir.IntType(32):
                if node.op == '+':
                    return self.builder.add(left, right)
                elif node.op == '-':
                    return self.builder.sub(left, right)
                elif node.op == '*':
                    return self.builder.mul(left, right)
                elif node.op == '/':
                    return self.builder.sdiv(left, right)
                elif node.op == '==':
                    return self.builder.icmp_signed('==', left, right)
                elif node.op == '!=':
                    return self.builder.icmp_signed('!=', left, right)
                elif node.op == '>':
                    return self.builder.icmp_signed('>', left, right)
                elif node.op == '<':
                    return self.builder.icmp_signed('<', left, right)
                elif node.op == '<>':
                    return self.builder.icmp_signed('<=', left, right)
            elif left.type == ir.DoubleType():
                if node.op == '+':
                    return self.builder.fadd(left, right)
                elif node.op == '-':
                    return self.builder.fsub(left, right)
                elif node.op == '*':
                    return self.builder.fmul(left, right)
                elif node.op == '/':
                    return self.builder.fdiv(left, right)

        
    def gen_print(self, val):
        # Upewniamy się, że @fmt istnieje w module tylko raz
        if self.fmt is None:
            fmt_str = "%d\n\0"
            fmt_type = ir.ArrayType(ir.IntType(8), len(fmt_str))
            self.fmt = ir.GlobalVariable(self.module, fmt_type, name="fmt")
            self.fmt.linkage = 'internal'
            self.fmt.global_constant = True
            self.fmt.initializer = ir.Constant(fmt_type, bytearray(fmt_str.encode("utf8")))

        # Wskaźnik na pierwszy element tablicy (typowe gep dla stringa w LLVM)
        if val.type == ir.IntType(32):
            fmt = self.get_or_create_fmt("%d\n")
        elif val.type == ir.DoubleType():
            fmt = self.get_or_create_fmt("%f\n")

        zero = ir.Constant(ir.IntType(32), 0)
        fmt_ptr = self.builder.gep(fmt, [zero, zero])

        printf = self.module.globals.get('printf')
        if printf is None:
            printf_ty = ir.FunctionType(ir.IntType(32), [ir.PointerType(ir.IntType(8))], var_arg=True)
            printf = ir.Function(self.module, printf_ty, name="printf")

        self.builder.call(printf, [fmt_ptr, val])



if __name__=="__main__":

    # Testing purpose
    
    #code = "x=5+15;wypisz(x);y=1;wypisz(x-y);"
    #code = "pi=3.14;wypisz(pi * pi);"
    #code = "liczbaA=4;wypisz(liczbaA* 2);"
    #code = "liczbaB=12;wypisz(liczbaB / 3);"
    #code = "liczbaC=4;wypisz(liczbaC* 2);"
    #code = "liczbaD=12.312;wypisz(liczbaD / 132.23);"
    #code = 'wczytaj(pi);wypisz(pi + 12);'
    #code = 'wypisz(1232);'

    code = """
            x = 26;
            jezeli (x > 3) {
                wypisz(x);
                wypisz(321);

            } inaczej {
                wypisz(0);
            }   
            """

    # Etap 1: Parsowanie kodu
    input_stream = InputStream(code)
    lexer = SnMsLangLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    tokens = CommonTokenStream(lexer)
    parser = SnMsLangParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    tree = parser.program()

    # Etap 2: AST Builder
    builder = ASTBuilder()
    walker = ParseTreeWalker()
    walker.walk(builder, tree)

    # Tutaj generujemy już AST
    ast = builder.get_ast()

    generator = IRGenerator()
    ir_code = generator.generate(ast)

    # Just printing, debug ON
    print(ir_code)

    with open("program.ll", "w") as f:
        f.write(ir_code)
