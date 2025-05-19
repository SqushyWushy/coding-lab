#include <stdio.h>
#include <stdlib.h>

int main(){
    int sum = 0, num;

    printf("Enter numbers to add(enter -1 to stop):\n");

    while(1){
        printf("Enter a number: ");
        scanf("%d", &num);

        if(num == -1){
            break;
        }

        sum += num;
        printf("Total so far: %d\n", sum);
    }

    printf("Final sum: %d\n", sum);
    return 0;
}
