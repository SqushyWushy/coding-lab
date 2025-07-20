// Description: Encrypt a message by shifting each letter by a user-provided key
// using Caesar’s cipher.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

string cipher(int key, string user_string);

int main(int argc, string argv[]) {
  // 1. Prompt the user for input, a single positive integer value
  // - use the main signature int main(int argc, string argv[])
  if (argc != 2) {
    printf("./caesar key");
    return 1;
  }

  // 2. Validate user input and include usage message with incorrect input
  // - first check number of arguments is correct
  // - also check to ensure its only numbers
  // - also check to ensure its not letters
  // - ensure it is only positive integer
  // - if it doesnt pass, then break out of program with usage instructions
  // - if it passes all of this then we need to store this "key" argument into
  // int variable
  // int key = atoi(argv[1]);

  int key = atoi(argv[1]);

  if (key <= 0) {
    printf("./caesar key\n");
    return 1;
  }

  // 3. Prompt user for input, a string - "plaintext: "[input]
  string user_string = get_string("plaintext: ");
  // 4. Create a function w/2 arguments, key and string
  // - takes string input and key input
  // - iterate through each char in string
  // - if char is letter, replace char with letter + key
  // - if not letter, keep char the same
  // - return the new string
  string result = cipher(key, user_string);
  // 5. Print the cipher text output - "ciphertext: "[output]
  // - store result of fucntion into string variable
  // - print the result
  printf("ciphertext: %s\n", result);
  //
  return 0;
}

string cipher(int key, string user_string) {
  int length = strlen(user_string);
  for (int i = 0; i < length; i++) {
    if (islower(user_string[i])) {
      user_string[i] = (((user_string[i] - 'a' + key) % 26) + 'a');
    } else if (isupper(user_string[i])) {
      user_string[i] = (((user_string[i] - 'A' + key) % 26) + 'A');
    }
    // else: it's not a letter -> do nothing and just let it pass through
  }
  return user_string;
}
