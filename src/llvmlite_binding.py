from llvmlite import binding

def initialize_llvm():
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

def create_target_machine():
    return binding.Target.from_default_triple().create_target_machine()

def compile_ir_to_machine_code(ir_code):
    with open("program.ll", "w") as f:
        f.write(ir_code)
    subprocess.run(["llc", "program.ll", "-o", "program.s"])
    subprocess.run(["gcc", "program.s", "-o", "program"])
