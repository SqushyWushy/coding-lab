package bounds;

/**
 * Jr Hector Gonzalez
 * 05/05/24
 * Use an exception class to identify whether or not the user's number is out of bounds
 * JDK 18.0.2.1
 */
import java.util.Scanner;

class OutOfBoundsException extends Exception{
    
    public OutOfBoundsException(){
    super("\nError: Invalid number. Not IN BETWEEN 1 and 10.");
    }
}

public class Bounds {
    public static int number(int number) throws OutOfBoundsException{
        if(number <= 1 || number >= 10){
            throw new OutOfBoundsException();
        }
        return number;
    }
            
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number between 1 and 10: ");
        int userChoice = scanner.nextInt(); 
        
        try{
            int choiceResult = number(userChoice);
            System.out.println("\nExcellent! " + choiceResult + " is indeed between 1 and 10!");
        }catch(OutOfBoundsException e){
            System.out.println(e.getMessage());
        }
        
    }
    
}
