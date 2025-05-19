#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int secretNumber;
    int guess;
    int min = 1;
    int max = 100;
    char response[10];
    int guessCounter = 0;

    srand(time(NULL));
    secretNumber = (rand() % 100) + 1;

    printf("The computer has picked a number between 1 and 100. Try to guess it!\n");
    guess = 0;
    while(guess != secretNumber){
        guessCounter++;
        printf("Enter your guess: ");
        scanf("%d", &guess);


        if(guess == secretNumber){
        
            printf("You got it! It took you %d tries!\n", guessCounter);
            break;
        }
        
        (guess > secretNumber) ? (printf("Guess lower!\n")) : (printf("Guess higher!\n"));
    }



    return 0;
}
