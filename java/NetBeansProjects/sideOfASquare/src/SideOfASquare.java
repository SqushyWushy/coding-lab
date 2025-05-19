/*
 * Jr Hector Gonzalez
 * 02/10/24
 * JDK 18.0.2.1
 * Objective: Calculate the area and perimeter of a square
 */
import java.util.Scanner;

public class SideOfASquare {
    public static void main(String[] args) {
       Scanner input = new Scanner(System.in);
       
       System.out.println("Enter the length of the side of your square: ");
       double squareSide = input.nextDouble();
       
       double areaSquare = calculateArea(squareSide);
       double perimeterSquare = calculatePerimeter(squareSide);
       
       System.out.println("\nThe length of one side of your square is " + squareSide);
       System.out.println("---------------------------------------------");
       System.out.println("The area of your square is " + areaSquare);
       System.out.println("The perimeter of your square is " + perimeterSquare);
       
    }
    
    public static double calculateArea(double squareSide){
        double areaSquare = squareSide * squareSide;
        
        return areaSquare;
    }
    
    public static double calculatePerimeter(double squareSide){
        double perimeterSquare = squareSide * 4;
        
        return perimeterSquare;
    }
    
}
