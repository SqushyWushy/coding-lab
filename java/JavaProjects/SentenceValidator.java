
/**
 * Jr Hector Gonzalez
 * 04/07/24
 * Validate a sentence written by the user
 * JDK 18.0.2.1
 */
import java.util.Scanner;

public class SentenceValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String sentence;
        
        System.out.println("Please enter a sentence using the following instructions.");
        System.out.println("1.The sentence must be between 3 and 50 characters long");
        System.out.println("2.The sentence must contain either a question mark, exclamation mark, or period.");
        System.out.println("3.The sentence must have at least one uppercase letter");
        System.out.println("4.The sentence must have at least one lowercase letter" + "\n");
        
        while(true){
            System.out.println("Please enter a sentence: ");
            sentence = scanner.nextLine();
            int upperCase = 0;
            int lowerCase = 0;
            
            for(int i = 0; i < sentence.length(); i++){
                if(Character.isUpperCase(sentence.charAt(i))){
                    upperCase++;
                }
            }
            
            for(int i = 0; i < sentence.length(); i++){
                if(Character.isLowerCase(sentence.charAt(i))){
                    lowerCase++;
                }
            }
            
            if(sentence.length() >= 3 && sentence.length() <= 50 && (sentence.contains("?") || sentence.contains("!") || sentence.contains(".")) && lowerCase > 0 && upperCase > 0){
                System.out.println("\n" + "Valid. You correctly followed the instructions!");
                break;
            }else{
                System.out.println("Invalid. Remember to correctly follow the instructions." + "\n");
            }
        }
    }
    
}
