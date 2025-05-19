#include <stdio.h>
#include <unistd.h>

int main(){
    pid_t pid = fork();

    if (pid > 0){
        printf("Parent: My PID is %d, my child's PID is %d\n", getpid(), pid);
    } else if(pid == 0){
        printf("Child: My PID is %d, my parent's PID is %d\n", getpid(), getppid());
    } else {
        printf("Fork Failed");
    }
    return 0;
}
