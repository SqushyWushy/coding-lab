#include <stdio.h>
#include <stdlib.h>


int main(){
    int min = 1;
    int max = 100;
    int guess;
    char response;

    printf("Think of a number between 1 and 100. I will guess it!\n");

    while(1){
        guess = (min + max) / 2;
        printf("Is your number less than(<), greater than(>) or equal(=) to %d? ", guess);
        scanf(" %c", &response);

        if (response == '='){
            printf("I guessed it! Your number is %d.\n", guess);
            break;
        }
        (response == '>') ? (min = guess + 1) : (max = guess - 1);
    }

    return 0;
}
