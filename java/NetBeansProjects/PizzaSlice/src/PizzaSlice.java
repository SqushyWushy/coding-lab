/*
 * Jr Hector Gonzalez
 * 02/04/2024
 * JDK Version 18.0.2.1
 * What percent of pizza did user use?
 */
import java.util.Scanner;

public class PizzaSlice {
    public static void main(String[] args) {
        double userPizzaSlices;
        double TOTAL_PIZZA = 8;
        Scanner input = new Scanner(System.in);
        System.out.println("How many slices of pizza would you like?(total of 8): ");
        userPizzaSlices = input.nextInt();
        double percentPizza = (userPizzaSlices/TOTAL_PIZZA)* 100;
        
        while(userPizzaSlices >= 0 && userPizzaSlices <= 8) {
            System.out.println("You ate " + percentPizza + " percent of the pizza.");
            
            break;          
        }
            
        }
            
        }
    
