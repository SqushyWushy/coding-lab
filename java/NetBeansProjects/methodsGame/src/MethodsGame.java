/*
 * Jr Hector Gonzalez
 * 02/09/24
 * JDK 18.0.2.1
 * Objective: Generate random facts about a planet and return whether it is
 * true or false
 */
import java.util.Scanner;

public class MethodsGame {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean playAgain = true;
        
        while(playAgain){
            int randomNumber = generateRandomNumber(1,10);
            boolean isFactTrue = switchPlanet(randomNumber);
            
            System.out.println("Is this fact true? Enter 1 for Yes, 0 for No: ");
            int userGuess = input.nextInt();
            
            compare(isFactTrue, userGuess);
            
            System.out.println("\nDo you want to play again? Enter 1 for Yes, 0 for No:");
            int userResponse = input.nextInt();
            
            if(userResponse == 1){
            playAgain = true;
        }else{
            playAgain = false;
            System.out.println("\nThank you for playing! I hope you learned"
                    + " something new!");
            }
            
            System.out.println();
        }
    }
    public static boolean switchPlanet(int number){
        boolean isFactTrue;
        switch(number){
            case 1: 
                System.out.println("Octopuses have three hearts");
                isFactTrue = true;
                
                break;
            case 2: 
                System.out.println("Cows have best friends");
                isFactTrue = true;
                
                break;
            case 3: 
                System.out.println("Butterflies taste with their feet");
                isFactTrue = true;
                
                break;
            case 4: 
                System.out.println("Elephants can't jump");
                isFactTrue = true;
                
                break;
            case 5: 
                System.out.println("The fingerprints of a koala are so "
                        + "indistinguishable from humans that they can "
                        + "contaminate crime scenes");
                isFactTrue = true;
                
                break;
            case 6: 
                System.out.println("Dolphins can fly");
                isFactTrue = false;
                
                break;
            case 7: 
                System.out.println("Penguins live in the Arctic");
                isFactTrue = false;
                
                break;
            case 8: 
                System.out.println("Snakes blink with their eyelids when sleeping");
                isFactTrue = false;
                
                break;
            case 9: 
                System.out.println("Giraffes communicate by mooing");
                isFactTrue = false;
                
                break;
            case 10: 
                System.out.println("All spiders have ten legs");
                isFactTrue = false;
                
                break;
            default: 
                System.out.println("Invalid number.");
                isFactTrue = false;
        }
        return isFactTrue;
    }
    
    public static void compare(boolean isFactTrue, int userGuess){
        if((isFactTrue && userGuess == 1) || (isFactTrue && userGuess == 0)){
            System.out.println("Correct!");
        }else {
            System.out.println("Incorrect!");
        }
        
    }
    
    public static int generateRandomNumber(int a, int b){
        double range = (Math.abs(a-b)+1);
        if (a <= b){
            return (int)(Math.random()*range+a);
        }else {
            return (int)(Math.random()*range+b);
        }
    }
    
    
}
