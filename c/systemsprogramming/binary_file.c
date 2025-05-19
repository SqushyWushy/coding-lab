#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char name[50]; //char array to store name -- max 50 char
    int age; //store age
    double gpa; //double to store gpa
    

    printf("Enter your full name: ");
    fgets(name, sizeof(name), stdin);

    name[strcspn(name, "\n")] = '\0';


    printf("Enter your age: ");
    scanf("%d", &age);

    printf("Enter your gpa: ");
    scanf("%lf", &gpa);

    FILE *file = fopen("simple.out", "wb");

    if (file == NULL){
        printf("Error opening file!\n");
        return 1;
    }
    
    fwrite(name, sizeof(name), 1, file);
    fwrite(&age, sizeof(age), 1, file);
    fwrite(&gpa, sizeof(gpa), 1, file);

    fclose(file);
        
    return 0;
}
