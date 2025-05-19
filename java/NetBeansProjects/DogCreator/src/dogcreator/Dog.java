/*
Jr Hector Gonzalez
02/24/24
JDK 18.0.2.1
Practice with setters and getters(mutators and accessors)
*/
package dogcreator;
public class Dog {
    //instance variable
    private String name = null;
    private double weight = 0;
    
    public Dog(String newName, double newWeight){
        name = newName;
        weight = newWeight;
    }
    
    public void setName(String newName){
        name = newName; 
    }
    
    public void setWeight(double newWeight){
        if(newWeight > 0){
            weight = newWeight;
        }else{
            System.out.println("Weight cannot be zero or negative.");
        }
    }
    public String getName(){
        return name;
    }
    
    public double getWeight(){
        return weight;
    }
    
    public String compare(Dog dogCompare){
        if(dogCompare.weight > this.weight){
            return dogCompare.name + " is heavier than " + this.name;
        }else if(dogCompare.weight < this.weight){
            return this.name + " is heavier than " + dogCompare.name;
        }else {
            return "The dogs weights are equal";
        }
    }
} //end of class
