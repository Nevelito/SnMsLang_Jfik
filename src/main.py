import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from ast_builder import parse_code
from ir_generator import IRGenerator, generate_machine_code

code = "x = 5 + 10;"

ast = parse_code(code)

ir_generator = IRGenerator()

for node in ast:
    ir_code = ir_generator.generate_ir(node)
    print(ir_code)

ir_code = ir_generator.get_ir_code()
generate_machine_code(ir_code)
