package bounds;

class OutOfBoundsException extends Exception{
    
    public OutOfBoundsException(){
    super("\nError: Invalid number. Not IN BETWEEN 1 and 10.");
    }
}
