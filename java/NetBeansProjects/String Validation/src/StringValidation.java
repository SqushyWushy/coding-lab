/**
 * Jr Hector Gonzalez
 * 04/07/24
 * This program will validate a string
 * JDK 18.0.2.1
 */
 import java.util.Scanner;

public class StringValidation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String email;
        
        System.out.println("Please enter an email address that contains the following:");
        System.out.println("1. Between 16 - 25 characters");
        System.out.println("2. An @ symbol");
        System.out.println("3. At least one digit." + "\n");
        
        while(true){
            System.out.println("Enter email address: ");
            email = input.nextLine();
            
            if(email.length() >= 15 && email.length() <= 25 && email.contains("@") && email.matches(".*[0-9].*")){
                System.out.println("\n" + "Successful Email Address!");
                break;
            }else{
                System.out.println("Invalid. Please read instructions carefully." + "\n");
            }
        }
    }       
}
