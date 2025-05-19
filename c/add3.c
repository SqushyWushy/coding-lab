#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char input[100]; // a buffer to store the input line

    while (1){
        printf("Enter numbers: ");
        fgets(input, 100, stdin); //this grabs what the user typed
        
        int sum = 0;
        char *piece = strtok(input, " "); //get first number
        

        while (piece != NULL){
            sum += atoi(piece);
            piece = strtok(NULL, " ");
        }
        
        printf("Total:  %d\n", sum);
    }

    return 0;
}
