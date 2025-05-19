#include <stdio.h>
#include <unistd.h>

int main(){
    int num = getpid() % 10 + 1; // Get PID, limit it to 1-10
    int sum = 0;

    //ask the user for a number
    printf("Using Process ID(PID as number: %d)\n", num);

    //print the multiplication table from 1 to 10
    for(int i = 1; i <=10; i++){
        printf("%d x %d = %d\n", i, num, i * num);
        sum += (i * num);
    }

    printf("Sum: %d\n", sum);
    return 0;
}
