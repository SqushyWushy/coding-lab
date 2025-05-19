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
