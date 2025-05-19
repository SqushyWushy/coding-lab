package squarecreator;

/**
 * Jr Hector Gonzalez
 * 03/29/24
 * Create a square class and encapsulate the concept of a square. 
 * I was unable to add multiple files to Canvas so I just added the other code
 * to the comments below.
 * JDK 18.0.2.1
 */
public class SquareCreator {
    public static void main(String[] args) {
        Square square1 = new Square(5);
        Square square2 = new Square(8);
        
        System.out.println("Square 1: " + "\n" + square1.toString());
        System.out.println();
        
        System.out.println("Square 2: " + "\n" + square2.toString()); 
        System.out.println();
        
        System.out.println("These squares are the same: " + square1.equals(square2));
    }
    
}

/*
package squarecreator;

public class Square {
    private int lengthOfSide;//instance variable
    
    public Square(int s){
        this.lengthOfSide = s;
    }
    public void setLengthOfSide(int s){
        lengthOfSide = s;
    }
    public int getLengthOfSide(){
        return lengthOfSide;
    }
    public int calculateArea(int s){
        return (lengthOfSide*lengthOfSide);
    }
    @Override
    public String toString(){
        return "Length of Side: " + this.lengthOfSide + "\n" + 
                "Area: " + this.calculateArea(lengthOfSide);
                
    }
    public boolean equals(Square square2){
        return this.lengthOfSide == square2.lengthOfSide;
    }
}
*/
