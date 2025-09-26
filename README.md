# 8051 Assembly Compiler (Python)
A functional single-pass assembler built in Python for a subset of the 8051 Microcontroller instruction set. This project was developed as a core component of the "CPU Architecture and Microcomputer Principles" coursework.

# Project Goal: Understanding Low-Level Execution
The primary objective was to demonstrate a hands-on understanding of how high-level mnemonics (like MOV or ADD) are translated into executable machine code (opcodes and operands).

This implementation provides practical insight into the core logic of a compiler/assembler, reinforcing concepts of instruction sets and CPU microarchitecture down to the gate level.

# Key Features & Technical Details
1. Instruction Parsing: Utilizes the Python re module for efficient lexical analysis and identification of instruction mnemonics, registers (Rn), and operand addressing modes.

2. Opcode Translation: Implements a high-speed lookup table (array of regex patterns and lambda actions) to perform rapid, one-to-one translation from assembly lines to hexadecimal machine code.

3. Targeted Instructions: Supports a foundational set of 8051 instructions, including key Data Transfer, Arithmetic, and Branching operations.

# How to Run the Compiler
Prerequisites
Python 3.x

Usage
Place the 8051 assembly code (one instruction per line) into the input file named test02.txt.

Run the compiler script:

```python compiler.py```

The resulting machine code (in sequential hexadecimal bytes) will be written to test02-out.txt.

Example Input (test01.txt)
```asm
MOV @R0, #7BH
MOV @R1, 6CH
SUBB A, 44H
CJNE A, #01H, 0F4H
MOV R4, #0A2H
ADD A, #93H
DJNZ 40H, 12H
MOV 48H, R5
ANL 38H, #77H
XRL 34H, A

```
Expected Output (test01-out.txt)
```76 7B A7 6C 95 44 B4 01 F4 7C A2 24 93 D5 40 12 8D 48 53 38 77 62 34 ```

# Key Takeaway for Performance
Working on this compiler demonstrated the direct relationship between assembly code structure and the resulting memory footprint. This experience informs my approach to writing performance-aware C++ code by considering:

1. Instruction Efficiency: Understanding the difference between one-byte and two-byte instructions.

2. Memory Layout: How compiler choices affect memory access patterns, which is critical for maximizing CPU Cache utilization in game engine development.

3. Documentation: For a detailed breakdown of the design decisions and technical analysis (in Mandarin), please refer to the Full Technical Report (PDF) located in the Documentation folder.
