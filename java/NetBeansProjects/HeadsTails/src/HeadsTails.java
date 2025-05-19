/* Jr Hector Gonzalez
   02/04/2024
   JDK 18.0.2.1 
   Tally tails and head count from coin toss
 */
import java.util.Scanner;
public class HeadsTails {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("How many times would you like to flip the coin? ");
        int times = input.nextInt();
        int headCounter = 0;
        int tailCounter = 0;
        for(int i = 0; i < times; i++){
            double r = Math.random();//generate a random number
            if (r >= .5){
                System.out.println("Heads");
                headCounter++;
            }else{
                System.out.println("Tails");
                tailCounter++;
            }
        }
        System.out.println("\nNumber of heads: " + headCounter
        + "\nNumber of tails: " + tailCounter);
    }
    
}
