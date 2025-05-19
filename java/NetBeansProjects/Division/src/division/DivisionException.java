package division;

class DivisionException extends Exception {
    
    public DivisionException(){
        super("Error: You cannot divide by zero");
    }
}
