#include <ctype.h> // for isprint()
#include <stdint.h>
#include <stdio.h>

#define BYTES_PER_LINE 16

int main(void) {
  FILE *file = fopen("card.raw", "r");
  if (file == NULL) {
    printf("Could not open card.raw\n");
    return 1;
  }

  uint8_t buffer[BYTES_PER_LINE];
  long offset = 0;

  // Read and display the file 16 bytes at a time
  while (fread(buffer, 1, BYTES_PER_LINE, file) == BYTES_PER_LINE) {
    // Print the offset
    printf("%08lx: ", offset);

    // Print each byte in hex
    for (int i = 0; i < BYTES_PER_LINE; i++) {
      printf("%02x ", buffer[i]);
    }

    printf(" ");

    // Print ASCII version
    for (int i = 0; i < BYTES_PER_LINE; i++) {
      if (isprint(buffer[i])) {
        printf("%c", buffer[i]);
      } else {
        printf(".");
      }
    }

    printf("\n");
    offset += BYTES_PER_LINE;
  }

  fclose(file);
  return 0;
}
