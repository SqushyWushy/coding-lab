public class SumCalculator {
    public static void main(String[] args) {
        int sum = 0;
        int number = 10; // Change this to any number to calculate sum up to that number
        for (int i = 1; i <= number; i++) {
            sum += i;
        }
        System.out.println("Sum from 1 to " + number + " is: " + sum);
    }
}
