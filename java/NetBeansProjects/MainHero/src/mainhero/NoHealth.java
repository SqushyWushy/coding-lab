package mainhero;

class NoHealth extends Exception{
    
    public NoHealth(){
        super("Error: The hero must be assigned health points");
    }
}
