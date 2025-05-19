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
