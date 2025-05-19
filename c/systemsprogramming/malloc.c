#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    int *ptr = malloc(sizeof(int));  // Ask for memory (sticky note)
    *ptr = 42;  // Write "42" on it

    pid_t pid = fork();  // Clone yourself

    if (pid == 0) {  // Child process
        printf("Child sees: %d at address %p\n", *ptr, ptr);
        *ptr = 100;  // Change the value in child's copy
        printf("Child changes value to: %d\n", *ptr);
    } else {  // Parent process
        sleep(1);  // Let child run first
        printf("Parent sees: %d at address %p\n", *ptr, ptr);
    }

    free(ptr);  // Clean up memory

    return 0;
}
