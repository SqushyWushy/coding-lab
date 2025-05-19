package nature;

/**
 * Jr Hector Gonzalez
 * 04/19/24
 * Print information about a specific tree using a Tree class and a FruitTree class
 * JDK 18.0.2.1
 */
public class Nature {
    public static void main(String[] args) {
        FruitTree appleTree = new FruitTree("Apple Tree", 20, "Apple");
        System.out.println(appleTree);
    }
    
}


//I used separate files to create my code but canvas is only allowing me to submit
//one file so I have added the other files as comments in my code below

/*package nature;

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


package nature;

public class FruitTree extends Tree {
    private String fruitType;
    
    public FruitTree(String name, int height, String fruitType){
        super(name, height);
        this.fruitType = fruitType;
    }
    
    public String getFruitType() {return fruitType;}
    public void setFruitType(String fruitType) {this.fruitType = fruitType;}
    
    public String toString(){
        return super.toString() + "\nFruit type: " + fruitType;
    }
}
*/