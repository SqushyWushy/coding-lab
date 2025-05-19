#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
    // loop through arguments in reverse order(start from last word)
    for(int i = argc - 1; i > 0; i--){
        int length = strlen(argv[i]); //get length of the word
        
        for(int j = length - 1; j >= 0; j--) {
            putchar(argv[i][j]);
        }

        putchar(' ');
    }

    putchar('\n');
    return 0;
}
