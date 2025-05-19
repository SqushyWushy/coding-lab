
package monthcreator;

/**
 * Jr Hector Gonzalez
 * 03/29/24
 * Create a month class that encapsulates the concept of a month
 * JDK 18.0.2.1
 */
public class MonthCreator {
    public static void main(String[] args) {
        Month month1 = new Month(2);
        Month month2 = new Month(2);
        
        System.out.println(month1.toString());
        System.out.println();
        
        System.out.println(month2.toString());
        System.out.println();
        
        if(month1.equals(month2)){
            System.out.println(month1.getMonthName() + " is equal to " +
                    month2.getMonthName());
        }else{
            System.out.println((month1.getMonthName() + " is not equal to " + 
                    month2.getMonthName()));
        }
    }
    
}
