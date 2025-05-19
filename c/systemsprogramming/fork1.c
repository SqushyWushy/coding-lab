#include <stdio.h>
#include <unistd.h>

int main(){
    fork(); //creates a child process
    printf("Hello from the process %d!\n", getpid());
    return 0;
}
