package division;

/**
 * Jr  Hector Gonzalez
 * 05/05/24
 * This program will test an exception class by using a basic division program
 * JDK 18.0.2.1
 */
import java.util.Scanner;

public class Division {
    public static double Divide(double numerator, double denominator) throws DivisionException{
        if(denominator == 0){
            throw new DivisionException();
        }
        return numerator/denominator;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the numerator: ");
        int numerator = scanner.nextInt();
        
        System.out.println("Enter the denominator: ");
        int denominator = scanner.nextInt();
        
        try{
            double result = Divide(numerator, denominator);
            
            System.out.println(numerator + " divided by " + denominator + " = " + result);
        }catch(DivisionException e){
           System.out.println(e.getMessage());
        }
    }
    
}
