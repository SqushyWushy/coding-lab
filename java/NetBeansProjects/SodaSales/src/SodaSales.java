/*
 * Jr Hector Gonzalez
 * 03/03/2024 
 * JDK 18.0.2.1
 */
import java.util.Scanner;//import to ask user for input

public class SodaSales {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);//new scanner object for input
    
        int typesOfSoda = 0;//initialize types of soda to zero
        
        while(typesOfSoda <= 0){//types of soda already at zero so as long as it stays
            //at zero then it will continue to ask the user for number of sodas
            System.out.println("----------------------------------------------");
            System.out.print("How many types of soda would you like to enter: ");
            typesOfSoda = input.nextInt();
            
            if(typesOfSoda <= 0){
                System.out.println("\nPlease enter a positive number.");
            }
        }
        input.nextLine(); //clear the scanner buffer
        
        //next step is to create an array for soda names and soda sales
        String[] sodaNames = new String[typesOfSoda];
        int[] totalSold = new int[typesOfSoda];
        
        //next step is to enter the soda names while making sure it's not negative
        for(int i = 0; i < typesOfSoda; i++){
            System.out.print("Enter the name of soda type " + (i + 1) + ": ");
            sodaNames[i] = input.nextLine();
        }
        // enter the number of cans sold for each type of soda
        for(int i = 0; i < typesOfSoda; i++){
            int sales = -1;
            while (sales < 0){
                System.out.print("Enter the number of " + sodaNames[i] + " bottles"
                + " sold: ");
                sales = input.nextInt();
                
                if (sales >= 0){
                    totalSold[i] = sales;
                }else{
                    System.out.println("Invalid entry. Must be 0 or greater.");
                }
            }
        }
        //calculate and display the results
        int allTotalSales = 0;
        int highestIndex = 0;
        int lowestIndex = 0; 
        
        for(int i = 0; i < totalSold.length; i++){
            allTotalSales += totalSold[i];
            
            if(totalSold[i] > totalSold[highestIndex]){
                highestIndex = i;
            }
            if(totalSold[i] < totalSold[lowestIndex]){
                lowestIndex = i;
            }
        }
        System.out.println("-----------------------------------------------");
        System.out.println("Total Sold: " + allTotalSales);
        System.out.println("Highest Sold: " + sodaNames[highestIndex]);
        System.out.println("Lowest Sold: " + sodaNames[lowestIndex]);
    }
    
}


/*
Example Output:
How many types of soda would you like to enter: -1
How many types of soda would you like to enter: 3
Enter the name of soda type 1: Sprite
Enter the name of soda type 2: Pepsi
Enter the name of soda type 3: Coke
Enter the number of Sprite bottles sold: -5
Enter the number of Sprite bottles sold: 125
Enter the number of Pepsi bottles sold: 107
Enter the number of Coke bottles sold: 203
------------------------------------------
Total Sold: 435
Highest Sold: Mountain Dew
Lowest Sold: Coke
*/
