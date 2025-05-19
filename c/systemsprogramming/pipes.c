#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main(){
    int pipe1[2];
    int pipe2[2];

    pipe(pipe1);
    pipe(pipe2);

    pid_t pid = fork();

    if (pid == 0){
        dup2(pipe1[0], 0);
        dup2(pipe2[1], 1);

        close(pipe1[1]);
        close(pipe2[0]);

        execl("./add", "add", NULL);
        perror("execl failed: No such file or directory");
        exit(1);
    } else if(pid > 0) {
        close(pipe1[0]);
        close(pipe2[1]);

        char input[] = "4 11\n";
        write(pipe1[1], input, strlen(input));
        close(pipe1[1]);
        
        char buffer[100];
        read(pipe2[0], buffer, sizeof(buffer));
        printf("Result from child: %s", buffer);
        close(pipe2[0]);

        wait(NULL);
    } else {
        perror("fork failed");
        return 1;
    }  
return 0;
}
