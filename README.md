# SnMsLang Compiler

This project implements a simple compiler for the SnMsLang language using ANTLR and LLVM.

## Files
- `ast_builder.py`: Responsible for parsing SnMsLang code and building the AST.
- `ir_generator.py`: Converts AST into LLVM IR.
- `SnMsLang.g4`: ANTLR grammar file for SnMsLang language.
- `llvmlite_binding.py`: Handles LLVM bindings for generating machine code.

## Requirements
- Python 3.x
- ANTLR 4
- LLVM (with llvmlite bindings)

## Setup
1. Install dependencies: `pip install llvmlite antlr4-python3-runtime`
2. Generate the lexer and parser from the ANTLR grammar: `antlr4 -Dlanguage=Python3 SnMsLang.g4`


## Running the Compiler
To run the compiler, use the following Python code:
```python
from ast_builder import parse_code
from ir_generator import IRGenerator

code = "x = 5 + 10"
ast = parse_code(code)

ir_generator = IRGenerator()
for node in ast:
 ir_code = ir_generator.generate_ir(node)
 print(ir_code)

# Save IR and generate machine code
ir_code = ir_generator.get_ir_code()
generate_machine_code(ir_code)
