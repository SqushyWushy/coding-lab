/*
 * Author: Hector Gonzalez
 * 
 * Description: This is a basic C program to practice working with Linked Lists, but this
 *              time I'm going to create a loop of nodes 1-10 rather than having to create
 *              10 nodes individually which takes a lot of time and screen space
 * 
 * Date: May 3rd, 2025
 */

#include <stdio.h>
#include <stdlib.h>

// Node Structure
typedef struct Node {
    int value;
    struct Node* next;
} Node;


int main(){
    Node* head = NULL;
    Node* current = NULL;

    // Loop to create 10 nodes
    for (int i = 1; i <= 10; i++){
        Node* newNode = malloc(sizeof(Node));
        newNode->value = i;
        newNode->next = NULL;

        if (head == NULL){
            head = newNode;
            current = head;
        } else {
            current->next = newNode;
            current = newNode;
        }
    }

    //Print all values in the Linked List
    printf("Linked List Contents:\n");
    current = head;
    while(current != NULL){
        printf("%d -> ", current->value);
        current = current->next;
    }
    printf("NULL\n");

    // Free all memory
    current = head;
    while (current != NULL){
       Node* temp = current;
       current = current->next;
       free(temp);
    }

    return 0;
}
