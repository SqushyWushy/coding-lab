#include <stdio.h>
#include <stdlib.h>

int main(){
    char name[50]; //char array to store name -- max 50 char
    int age; //store age
    double gpa; //double to store gpa
    
    FILE *file = fopen("simple.out", "rb");

    if (file == NULL){
        printf("Error opening file!\n");
        return 1;
    }
    
    fread(name, sizeof(name), 1, file);
    fread(&age, sizeof(age), 1, file);
    fread(&gpa, sizeof(gpa), 1, file);

    printf("Full name: %s\n", name);
    printf("Age: %d\n", age);
    printf("GPA: %lf\n", gpa);

    fclose(file);
        
    return 0;
}
