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