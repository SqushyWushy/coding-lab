#include <stdio.h>

int main(){
    int num;
    int sum = 0;

    //ask the user for a number
    printf("Enter a number: ");
    scanf("%d", &num);

    //print the multiplication table from 1 to 10
    for(int i = 1; i <=10; i++){
        printf("%d x %d = %d\n", i, num, i * num);
        sum += (i * num);
    }

    printf("Sum: %d\n", sum);
    return 0;
}
