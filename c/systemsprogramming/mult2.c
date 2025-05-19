#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    //check if the user provided  an argument
    if (argc != 2){
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }

    int num = atoi(argv[1]);
    int sum = 0;

    //print the multiplication table from 1 to 10
    for(int i = 1; i <=10; i++){
        printf("%d x %d = %d\n", i, num, i * num);
        sum += (i * num);
    }

    printf("Sum: %d\n", sum);
    return 0;
}
