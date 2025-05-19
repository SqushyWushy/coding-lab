/*
Jr Hector Gonzalez
02/24/24
JDK 18.0.2.1
Practice with setters and getters(mutators and accessors)
*/
package dogcreator;
public class DogCreator {

    public static void main(String[] args) {
         Dog dog1 = new Dog("Texie", 25);
         Dog dog2 = new Dog("Juicy", 15);
         Dog dog3 = new Dog("Penny", 28);
         
         System.out.println("Name: " + dog1.getName());
         System.out.println("Weight: " + dog1.getWeight());
         
         System.out.println("Name: " + dog2.getName());
         System.out.println("Weight: " + dog2.getWeight());
         
         System.out.println("Name: " + dog3.getName());
         System.out.println("Weight: " + dog3.getWeight());
         
         dog3.setWeight(23);
         System.out.println(dog1.compare(dog2));
         System.out.println(dog2.compare(dog3));
         System.out.println(dog3.compare(dog1));
    }
    
}
