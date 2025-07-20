// Description: This program analyzes a block of text and estimates the U.S.
// grade level required to understand it using the Coleman-Liau index. It
// calculates the number of letters, words, and sentences in the text, then uses
// these values to compute a readability score. Based on the score, it outputs
// the appropriate grade level (e.g., “Grade 5”, “Before Grade 1”, or “Grade
// 16+”).

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void) {
  // Step 1: Prompt the user for text input
  // -- if no input at all, prompt the user until they provide input
  // -- any input works, as long as the user enters something
  string text = NULL;
  do {
    text = get_string("Text: ");
  } while (text == NULL || strlen(text) == 0);

  // Step 2: Count number of letters
  // -- we need to iterate through string and count every letter A - Z and a-z
  // -- if there is anything that is not a letter, it does not count

  // Step 3: Count number of words
  // -- we need to iterate through the string and increase the word count by 1
  // each time we read a space ' '
  // --remember anything that is not a space does nothing to the word count

  // Step 4: Count number of sentences
  // -- we need to iterate through the string and increase the sentence count by
  // 1 each time we come across any punctuation like ! or , or . or ?
  // -- however what if we come across something like ... or !! or ?? to solve
  // this we will only increase the count if the punctuation is followed by a
  // space for example "! " or "? " or ". "
  int letters = 0;
  int words = 1;
  int sentences = 0;

  for (int i = 0; text[i] != '\0'; i++) {
    if (isalpha(text[i])) {
      letters++;
    }
    if (text[i] == ' ') {
      words++;
    }
    if ((text[i] == '.' || text[i] == '!' || text[i] == '?') &&
        ((text[i + 1] == ' ' || text[i + 1] == '\0'))) {
      sentences++;
    }
  }
  //  printf("letters: %d\n", letters);
  //  printf("words: %d\n", words);
  //  printf("sentences: %d\n", sentences);

  // Step 5: Calculate the Coleman-Liau
  // -- first we need to calculate L = average number of letters per 100 words
  // -- second we need to calculate S = average number of sentences per 100
  // words
  // -- plug this into the formula Index = 0.0588 * L - 0.296 * S - 15.8
  // -- finally, we save this result, round it to the nearest integer and store
  // into a variable grade
  float l;
  float s;
  int result;

  l = ((float)letters / words) * 100;
  s = ((float)sentences / words) * 100;
  result = round(0.0588 * l - 0.296 * s - 15.8);
  // printf("l: %f\n", l);
  // printf("s: %f\n", s);
  // printf("result: %d\n", result);

  // Step 6: Print the grade level using the rules above
  // -- if grade < 1 print "Before Grade 1"
  // -- if grade >= 16, print Grade 16+
  // -- else just print the grade
  if (result < 1) {
    printf("Before Grade 1\n");
  } else if (result >= 16) {
    printf("Grade 16+\n");
  } else {
    printf("Grade %d\n", result);
  }

  return 0;
}
