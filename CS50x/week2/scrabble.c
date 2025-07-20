// Description: Prompts two players for words, calculates Scrabble scores, and
// declares the winner.
// -----------
// Steps:
// 1. Declare our variables: We need an array that holds the value for each
// letter in the Alphabet so a total of 26 values, we also need a score counter
// for each player. I think this is it for now but I'll come back if I think of
// any more. Also we will know the value of the char by doing index math!
// 2. Prompt the first user for their word
// 3. Prompt the second user for their word
// 4. Validate user input, it might be a good idea to create a function that
// validates user input since we have to do it twice, hmm or maybe create a for
// loop that runs twice? but we have 2 users in which input needs to be
// validated, so im thinking we need to create a function that needs to return
// true or false so maybe a do while loop that stays in the loop but the thing
// is we need to see true twice wait but there is no invalid input techincally,
// because if there is anything other than letters, we still count it but its
// zero so we simply need to make a fucntion that validates input then I think
// for now! we will pretty much create a funtion that accepts the each user
// input after user enters their word!
// 5. Once we have user input validated we have another,,, actually i just
// realized but we simply need to to take one user's input, validate and then
// get the score all together, and once we have gotten the score, then we are
// all done and we simply just do it again!
// 6. Once we have the score from both user's then we simply need to compare the
// scores and we are going to find the person that has the higher score so if
// user 1 is > user 2 than user 1 wins, else user 2 wins!
// 7. Print the winner and boom that is the end of the game, I think the hardest
// part is going to be the creation of the function.
// 8. Function will look like this: PASS in the word written by the user; check
// word char by char in C, increase the score by the value of each char by
// comparing it with the array and getting the value of the score

#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>

// Create a fucntion that validates the string
bool isValidWord(string word) {
  for (int i = 0; word[i] != '\0'; i++) {
    if (word[i] == ' ') {
      return false;
    }
  }
  return true;
}

// Create a fucntion that takes in user input/chosen word and outputs word score
int word_score(string word) {

  int final_score = 0;
  int char_value[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                        1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
  for (int i = 0; word[i] != '\0'; i++) {
    char ch = tolower(word[i]);

    if (ch >= 'a' && ch <= 'z') {
      int char_score = 0;
      int index = ch - 'a';
      char_score = char_value[index];
      final_score += char_score;
    }
  }

  return final_score;
}

int main() {
  // declare global variables
  string word1;
  string word2;
  int score1;
  int score2;
  // validate user1 string
  do {
    word1 = get_string("Player 1: ");
  } while (!isValidWord(word1));

  do {
    word2 = get_string("Player 2: ");
  } while (!isValidWord(word2));

  // calculate scores for user1 and user2
  score1 = word_score(word1);
  score2 = word_score(word2);

  // identify whose score is greater and print out the appropriate output!
  if (score1 == score2) {
    printf("Tie!\n");
  } else if (score1 > score2) {
    printf("Player 1 wins!\n");
  } else {
    printf("Player 2 wins!\n");
  }

  return 0;
}
