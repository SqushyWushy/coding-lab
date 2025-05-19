#include ""
#include <stdio.h>
#include <stdlib.h>

int main() {
  int N; // variable to store the number of integers

  printf("How many numbers do you want to enter?");
  scanf("%d", &N);

  int *numbers = (int *)malloc(N * sizeof(int));
  if (numbers == NULL) {
    printf("Memory allocation failed\n");
    return 1;
  }

  printf("Enter %d numbers:\n", N);
  for (int i = 0; i < N; i++) {
    printf("Number %d: ", i + 1);
    scanf("%d", &numbers[i]);
  }

  FILE *binFile = fopen("array.out", "wb");
  if (binFile == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  FILE *textFile = fopen("array.txt", "w");
  if (textFile == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  fwrite(numbers, sizeof(int), N, binFile);

  for (int i = 0; i < N; i++) {
    fprintf(textFile, "%d\n", numbers[i]);
  }

  fclose(binFile);
  fclose(textFile);

  free(numbers);

  printf("Data successfully written to both file!\n");

  return 0;
}
