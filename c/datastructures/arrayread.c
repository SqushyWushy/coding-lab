#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *file;
    int N;
    int *numbers;

    file = fopen("array.out", "rb");

    if (file == NULL){
        printf("Error opening file!\n");
        return 1;
    }
    
    fread(&N, sizeof(int), 1, file);

    numbers = (int *) malloc(N * sizeof(int));
    if (numbers == NULL){
        printf("Memory allocation failed!\n");
    }
    
    fread(numbers, sizeof(int), N, file);

    printf("Numbers in file: \n");
    for (int i = 0; i < N; i++){
        printf("%d ", numbers[i]);
    }
    
    printf("\n");

    fclose(file);
    free(numbers);

    return 0;
}
