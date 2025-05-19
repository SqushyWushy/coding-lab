.global _main
.extern _printf

.section __DATA,__data
message:
    .asciz "Hello, World!\n"

.section __TEXT,__text
_main:
    // Load the address of message into X0 (first argument for printf)
    adrp x0, message@PAGE
    add x0, x0, message@PAGEOFF
    bl _printf // Call printf

    // Exit the program (return 0)
    mov x0, 0  // Return value (0)
    mov x16, 1 // sys_exit
    svc #0x80  // System call
