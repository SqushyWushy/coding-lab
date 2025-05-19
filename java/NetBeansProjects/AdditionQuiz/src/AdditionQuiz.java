/*
 * Jr Hector Gonzalez
 * 02/04/2024
 * JDK 18.0.2.1
 * We will be grading an addition quiz with randomly generated numbers
 */
import java.util.Scanner;

public class AdditionQuiz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numberOfQuestions;
        
        // Loop until the user enters a valid number of questions
        while (true) {
            System.out.print("How many questions would you like to solve? ");
            numberOfQuestions = scanner.nextInt();
            if (numberOfQuestions >= 0) {
                break;
            }
            System.out.println("Please enter a number of 0 or greater.");
        }
        
        int correctAnswers = 0;
        for (int i = 0; i < numberOfQuestions; i++) {
            // Generate two random numbers between 1 and 50
            int number1 = (int) (Math.random() * 50) + 1;
            int number2 = (int) (Math.random() * 50) + 1;
            int correctAnswer = number1 + number2;
            
            // Ask the user to solve the equation
            System.out.print(number1 + " + " + number2 + " = ? ");
            int userAnswer = scanner.nextInt();
            
            // Check if the answer is correct
            if (userAnswer == correctAnswer) {
                System.out.println("Correct");
                correctAnswers++;
            } else {
                System.out.println("Incorrect");
            }
        }
        
        // Calculate the percentage of correct answers
        double percentageCorrect = ((double) correctAnswers / numberOfQuestions) * 100;
        
        // Display the results
        System.out.println("You got " + correctAnswers + " out of " + numberOfQuestions + " correct which is " + percentageCorrect + "%.");
        
        // Determine if the user passed or failed
        if (percentageCorrect >= 70) {
            System.out.println("You passed this addition quiz. Congratulations!");
        } else {
            System.out.println("You did not pass this addition quiz. Please try again.");
        }
        
        scanner.close();
    }
}

