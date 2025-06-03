CS 2340 Computer Architecture (3 semester credit hours) This course introduces the concepts of computer architecture by going through multiple levels of abstraction, and the numbering systems and their basic computations. It focuses on the instruction-set architecture of the MIPS machine, including MIPS assembly programming, translation between MIPS and C, and between MIPS and machine code. General topics include performance calculation, processor datapath, pipelining, and memory hierarchy.
⸻

1. Number Systems
   • Binary (1010), Decimal (10), Hex (0xA)
   • 2’s Complement for negatives
   • Bitwise operations: AND, OR, NOT, SHIFT

⸻

2. MIPS Assembly Language
   • MIPS = a simple assembly language used to teach CPU-level coding
   • No for loops, no int, just raw instructions like:

addi $t0, $zero, 5 # t0 = 5
add $t1, $t0, $t0 # t1 = 5 + 5 = 10

⸻

3. Registers & Memory
   • MIPS has 32 general-purpose registers ($t0, $s0, etc.)
	•	Stack ($sp), return address ($ra), program counter (PC)
   • Learn how memory is accessed with lw (load word), sw (store word)

lw $t0, 0($sp) # load from memory address in $sp

⸻

4. Instruction Types
   • R-type: register ops (add, sub)
   • I-type: immediate values (addi, lw)
   • J-type: jumps (j, jal)

⸻

5. How C Translates to Assembly
   • You manually convert:
   • C if-statements ➜ MIPS branches (beq, bne)
   • C loops ➜ MIPS jumps
   • C function calls ➜ stack frame management, jal, jr

This gives you insight into how real compilers work.

⸻

6. Machine Code
   • You learned how to manually convert MIPS assembly into binary machine code (e.g., 000000 01000 01001 01010 00000 100000 = add $t2, $t0, $t1)

⸻

7. Performance Metrics
   • Clock cycles, CPI (cycles per instruction)
   • Amdahl’s Law

Speedup = 1 / ( (1 - improvement%) + (improvement% / speedup_factor) )

⸻

8. Processor Datapath
   • You learned how the CPU is wired together — the ALU, control unit, registers, memory, etc.
   • You could probably draw a single-cycle datapath diagram showing how instructions flow.

⸻

9. Pipelining
   • Like an assembly line for instructions
   • Learn how pipelining increases performance by overlapping instruction execution
   • Also learn about hazards (when pipeline stages interfere)

⸻

10. Memory Hierarchy
    • Registers → Cache → RAM → Disk
    • You learned about locality, cache misses, and why some code runs faster just due to memory layout.

⸻
