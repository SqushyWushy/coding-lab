// We are going to solve the problem step by step just using words
// 1. Print out "Change owed: "
// 2. Ask the user for "Change amount"
// 3. Validate the input by ensuring. input is more than 0
// 4. If 0 or 100, then the output is just 0 and if outside boundaries, then ask
// user for input again
// 5. Create a list of 4 integers, coins[25, 10, 5, and 1]
// 6. Change amount = user input
// 7. Create variable "coin count" from integer division and variable "remainder
// from modular division
// 8. divide the change amount by 25 using integer division
// 9. divide the same change amount by 25 using modular division to get the
// remainder
// 10. Update the change amount variable from the remainder operation
// 11. Update the coin count variable and update the remainder variable
// 12. Now do that same process with 10 cents, 5 cents, and 1 cent
// 13. Do this until we get a remainder 0f 0
// 14. Print out the coin count
// Now the tricky part is going to be the creation of the loop!

#include <cs50.h>
#include <stdio.h>

int main() {
  // Initialize variables
  int coin_count = 0;
  int remainder;
  int length;
  int change_amount;
  int coins[4] = {25, 10, 5, 1};

  do {
    // Ask for user input
    change_amount = get_int("Change owed: ");
    // Validate user input
    if (change_amount < 0) {
      continue;
    } else {
      break;
    }
  } while (true);

  // get the length of our numbers array
  length = sizeof(coins) / sizeof(coins[0]);
  // create for loop for the part of the program that does all the work
  for (int i = 0; i < length; i++) {
    // increment the coin count
    coin_count += (change_amount / (coins[i]));
    // update the remainder to get the new change_amount
    remainder = change_amount % (coins[i]);
    // update the change_amount
    change_amount = remainder;
    // break out of loop if change_amount is 0 and print the coin count
    if (change_amount == 0) {
      printf("%d\n", coin_count);
      // break to avoid unneccesary steps
      break;
    }
  }

  // end of program successfully returns 0
  return 0;
}
