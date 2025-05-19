#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    //seed the random number generator
    srand(time(0));

    int num = (rand() % 10) + 1;
    int sum = 0;

    //ask the user for a number
    printf("Random number: %d\n", num);
    printf("Multiplication Table for %d:\n", num);

    //print the multiplication table from 1 to 10
    for(int i = 1; i <=10; i++){
        printf("%d x %d = %d\n", i, num, i * num);
        sum += (i * num);
    }

    printf("Sum: %d\n", sum);
    return 0;
}
