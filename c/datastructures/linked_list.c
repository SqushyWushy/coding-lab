/*
 * Author: Hector Gonzalez
 *
 * Description: This is a basic C program to practice working with Linked Lists,
 * creating nodes, and printing out the values inside those nodes.
 *
 * Date: May 3rd, 2025
 */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// Node Structure
typedef struct Node {
  int value;
  struct Node *next;
} Node;

int main() {
  // declare head node
  Node *head = malloc(sizeof(Node));
  head->value = 10;
  head->next = NULL;

  // declare second node
  Node *second = malloc(sizeof(Node));
  second->value = 20;
  second->next = NULL;

  // link first node to the second node
  head->next = second;

  printf("Head node value: %d\n", head->value);
  printf("Second node value: %d\n", head->next->value);

  // Free memory
  free(head);
  free(second);

  return 0;
}
