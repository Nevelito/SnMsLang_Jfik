from llvmlite import binding, ir
from ast_builder import parse_code

class IRGenerator:
    def __init__(self):
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

        self.module = ir.Module(name="program")
        self.context = ir.Context()
        self.builder = None

        self.target_triple = binding.get_default_triple()
        self.module.triple = self.target_triple
        self.target_machine = binding.Target.from_triple(self.target_triple).create_target_machine()

    def generate_ir(self, node):
        if isinstance(node, VariableNode):
            return f"@{node.name} = global i32 0, align 4"
        elif isinstance(node, ArithmeticOperationNode):
            left_ir = self.generate_ir(node.left)
            right_ir = self.generate_ir(node.right)
            if node.operator == '+':
                return f"add i32 {left_ir}, {right_ir}"
        elif isinstance(node, PrintNode):
            expr_ir = self.generate_ir(node.expression)
            return f"call void @print(i32 {expr_ir})"
        return ""

    def get_ir_code(self):
        return str(self.module)

def generate_machine_code(ir_code):
    with open("program.ll", "w") as f:
        f.write(ir_code)

    import subprocess
    subprocess.run(["llc", "program.ll", "-o", "program.s"])
    subprocess.run(["gcc", "program.s", "-o", "program"])

if __name__ == "__main__":
    code = "x = 5 + 10;"
    ast = parse_code(code)
    ir_generator = IRGenerator()

    for node in ast:
        ir_code = ir_generator.generate_ir(node)
        print(ir_code)

    ir_code = ir_generator.get_ir_code()
    generate_machine_code(ir_code)
