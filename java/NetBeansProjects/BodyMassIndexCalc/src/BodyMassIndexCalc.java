/*
 * Jr Hector Gonzalez
 * 02/09/24
 * JDK 18.0.2.1
 * Objective: allow a user to enter their height and weight and calculate their 
 * BMI using a message box
 */
import java.text.DecimalFormat;
import javax.swing.JOptionPane;

public class BodyMassIndexCalc {
    public static void main(String[] args) {
        String response;
        response = JOptionPane.showInputDialog(null, 
                "Enter your height in inches: ");
        double height = Double.parseDouble(response);
        response = JOptionPane.showInputDialog(null,
                "Enter your weight in pounds");
        double weight = Double.parseDouble(response);
        double bmi = calculateBMI(height, weight);
        DecimalFormat pattern = new DecimalFormat("###.00");
        JOptionPane.showMessageDialog(null, "Height: " + height +
                "\nWeight: " + weight + 
                "\nBMI: " + pattern.format(bmi));
    }
    public static double calculateBMI(double height, double weight){
        return (weight*703)/(height*height);
    }
}
