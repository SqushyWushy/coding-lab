import java.util.Scanner;

//import java.util.Arrays;

public class LabProgram {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //Read how many elements we want in the array
        int numValues = scanner.nextInt();
        //Declare an array with a double datatype
        double[] numbers = new double[numValues];
        //Collect the values for the array
        for (int i = 0; i < numValues; i++) {
            numbers[i] = scanner.nextDouble();
        }
        //Loop through the values in the array to identify the largest value
        double maxValue = numbers[0];
        for (int i = 1; i < numValues; i++) {
            if (numbers[i] > maxValue) {
                maxValue = numbers[i];
            }
        }
        //Divide each element in the array by the largest value
        for (int i = 0; i < numValues; i++) {
            numbers[i] = numbers[i] / maxValue;
            //Print with proper formatting
            System.out.printf("%.2f ", numbers[i]);
        }
        System.out.println();
    }
}
