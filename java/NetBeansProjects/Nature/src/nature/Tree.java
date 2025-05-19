package nature;

public class Tree {
    private String name;
    private int height;
    
    public Tree(String name, int height){
        this.name = name;
        this.height = height;
    }
    
    public String getName() {return name;}
    public void setName(String name) {this.name = name;}
    
    public int getHeight() {return height;}
    public void setHeight(int height) {this.height = height;}
    
    public String toString(){
        return "Name: " + name + "\nHeight: " + height;
    }
}
