package mainhero;

/**
 * Jr Hector Gonzalez
 * 05/07/24
 * This program tells a hero how many health points they have!
 * JDK 18.0.2.1
 */

public class MainHero {
    public static void main(String[] args) {
        
        Hero hero[] = new Hero[3];
        hero[0] = new Hero(40);
        hero[1] = new Hero(60);
        hero[2] = new Elf(80, "Archery Superiority");
        for (Hero hero1 : hero) {
            System.out.println(hero1);
        }

    }
    
}



/*package mainhero;

public class Hero{
    private int startingHealth;
    
    public Hero(int startingHealth){
        this.startingHealth = startingHealth;
    }
    
    public int getStartingHealth() {return startingHealth;}
    public void setStartingHealth(int startingHealth){
        this.startingHealth = startingHealth;
    }
    @Override
    public String toString(){
        return "I am a hero! I have " + startingHealth + " points.";
    }
}


package mainhero;


public class Elf extends Hero{
    private String specialPower;

    public Elf(int startingHealth, String specialPower) {
        super(startingHealth);
        this.specialPower = specialPower;
    }
    public String getSpecialPower(){
        return specialPower;
    }
    public void setSpecialPower(String specialPower){
        this.specialPower = specialPower;
    }
    public String toString(){
        return super.toString() + " My special power is " + specialPower + ".";
    }
    
}

package mainhero;

class NoHealth extends Exception{
    
    public NoHealth(){
        super("Error: The hero must be assigned health points");
    }
}


*/