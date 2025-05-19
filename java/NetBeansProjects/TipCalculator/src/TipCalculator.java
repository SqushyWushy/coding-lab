/*
 * Program: Computing tip amount
 * Name: Jr Hector Gonzalez
 * Date: 01/27/24
 * JDK Version: 18.0.2.1
 */
import javax.swing.JOptionPane;
import java.text.NumberFormat;
public class TipCalculator {
    public static void main(String[] args) {
        String input = JOptionPane.showInputDialog(null, "Enter the total bill");
        double bill = Double.parseDouble(input);
        input = JOptionPane.showInputDialog(null, "Enter the tip percentage"
                + " as a decimal");
        double percentage = Double.parseDouble(input); 
        
        double tipAmount = bill * percentage;
        double percentageConverted = percentage*100;
        NumberFormat formatter = NumberFormat.getCurrencyInstance();
        JOptionPane.showMessageDialog(null, "Bill Amount: " +formatter.format(bill) +
                "\nTip Percentage: " + percentageConverted + "%" +
                "\nTip Amount: "+ formatter.format(tipAmount));
    }
    
}
