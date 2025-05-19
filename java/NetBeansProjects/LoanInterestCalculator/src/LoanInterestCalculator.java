/*
 * Program: Calculate interest from a loan
 * Name: Jr Hector Gonzalez
 * Date: 01/27/24
 * JDK Version: 18.0.2.1
 */
import javax.swing.JOptionPane;
import java.text.NumberFormat;

public class LoanInterestCalculator {
    public static void main(String[] args) {
        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance();
        String amountString = JOptionPane.showInputDialog("Enter Loan Amount: ");
        double amount = Double.parseDouble(amountString);
        
        String rateString = JOptionPane.showInputDialog("Enter interest rate (%): ");
        double rate = Double.parseDouble(rateString);
        
        String yearsString = JOptionPane.showInputDialog("Enter number of years: ");
        int years = Integer.parseInt(yearsString);
        
        double interest = amount * (rate/100) * years;
        
        JOptionPane.showMessageDialog(null, 
                "Loan amount is: " + currencyFormat.format(amount) 
        + "\nInterest rate is: " + rate + "%"
        + "\nNumber of years: " + years
        + "\nInterest: " + currencyFormat.format(interest));
        
    }
    
}
