#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    //check if the user provided  an argument
    if (argc < 2){
        printf("Usage: %s <num1> <num2> <num3>...\n", argv[0]);
        return 1;
    }

    int sum = 0;

    for(int i = 1; i < argc; i++){
        sum += atoi(argv[i]);
    }

    printf("Sum: %d\n", sum);
    return 0;
}
