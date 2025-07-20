// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned int word_count = 0;

// Represents a node in a hash table
typedef struct node {
  char word[LENGTH + 1];
  struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word) {
  // TODO
  char temp[LENGTH + 1];
  int len = strlen(word);

  for (int i = 0; i < len; i++) {
    temp[i] = tolower(word[i]);
  }
  temp[len] = '\0';

  unsigned int index = hash(temp);
  node *cursor = table[index];

  while (cursor != NULL) {
    if (strcasecmp(cursor->word, temp) == 0) {
      return true;
    }
    cursor = cursor->next;
  }

  return false;
}

// Hashes word to a number
unsigned int hash(const char *word) {
  // TODO: Improve this hash function
  unsigned long hash = 5381;
  int c;
  while ((c = *word++)) {
    hash = ((hash << 5) + hash) + tolower(c); // hash * 33 + c
  }
  return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary) {
  FILE *file = fopen(dictionary, "r");
  if (file == NULL) {
    return false;
  }

  char word[LENGTH + 1];

  while (fscanf(file, "%s", word) != EOF) {
    node *new_node = malloc(sizeof(node));
    if (new_node == NULL) {
      fclose(file);
      return false;
    }

    strcpy(new_node->word, word);
    unsigned int index = hash(word);

    new_node->next = table[index];
    table[index] = new_node;

    word_count++;
  }

  fclose(file);
  return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void) {
  // TODO
  return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void) {
  // TODO
  for (int i = 0; i < N; i++) {
    node *cursor = table[i];
    while (cursor != NULL) {
      node *temp = cursor;
      cursor = cursor->next;
      free(temp);
    }
  }
  return true;
}
