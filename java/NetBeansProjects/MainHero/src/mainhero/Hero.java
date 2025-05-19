package mainhero;

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

