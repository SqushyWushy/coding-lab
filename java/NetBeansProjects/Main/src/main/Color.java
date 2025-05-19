package main;

public class Color {
    private int red;
    private int green;
    private int blue;
    
    public Color(int r, int g, int b) {
        red = r;
        green = g;
        blue = b;   
    }
    
    @Override
    public String toString(){
        return "#" + "(" + red +  "," + green + "," + blue + ")";
    }
}
