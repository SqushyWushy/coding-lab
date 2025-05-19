#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    fork();
    fork();
    fork();
    
    wait(NULL);
    printf("Process ID: %d, Parent ID: %d\n", getpid(), getppid());
    return 0;
}
