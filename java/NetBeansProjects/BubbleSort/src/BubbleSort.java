/*
 * Jr Hector Gonzalez
 * 03/03/2024
 * JDK 18.0.2.1 
 * sort a list of numbers in an
 * array and print out the sorted array.
 */
public class BubbleSort {    
    public static void main(String[] args) {
        int number[] = {8, 5, 3, 2, 9};
        boolean swap = true;
        int temp;
        
        while (swap == true){
            swap = false;
            for (int i = 0; i < number.length - 1; i++){
                if (number[i] > number[i+1]) {
                    temp = number[i + 1];
                    number[i+1] = number[i];
                    number[i] = temp;
                    swap = true;
                }
            }
        }
        for (int i = 0; i < number.length; i++){
            System.out.println(number[i]);
        }
    }
    
}
