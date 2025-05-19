#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
// Loop through all arguments starting from argv[1]
    for (int i = 1; i < argc; i++) {
        // Check if the length of the argument is NOT 5
        if (strlen(argv[i]) != 5) {
            printf("Bad!\n");  // If any word is not length 5, print "Bad!"
            return 0;          // Exit immediately
        }
    }
    // If all words are length 5, print "Good!"
    printf("Good!\n");
    return 0;
}
