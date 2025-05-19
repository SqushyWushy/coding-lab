/*
 * Program: Calculate the area and perimeter of a rectangle
 * Name: Jr Hector Gonzalez
 * Date: 01/28/24
 * JDK Version: 18.0.2.1
 */
import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class RectangeArea {
    public static void main(String[] args) {
        DecimalFormat formatter = new DecimalFormat("#0.00");
        String lengthStr = JOptionPane.showInputDialog("Enter length of the rectangle: ");
        double length = Double.parseDouble(lengthStr);
        
        String widthStr = JOptionPane.showInputDialog("Enter width of the rectangle: ");
        double width = Double.parseDouble(widthStr);
        
        double areaRectangle = length * width;
        double perimeterRectangle = (2 * length) + (2 * width);
        
        JOptionPane.showMessageDialog(null,
                "Lenth of the Rectangle: " + length +
                "\nWidth of the Rectangle: " + width +
                "\nArea: " + formatter.format(areaRectangle) +
                "\nPerimeter: " + formatter.format(perimeterRectangle));
    }
    
}
