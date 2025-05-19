/*
 * Jr Hector Gonzalez
 * 02/25/24
 * JDK 18.0.2.1
 * This program is a book class to encapsulate the concept of a book
 */
public class Book {
    private String title = null; //instance variable for the the title of the book
    private int numberofPages = 0; // another for the number of pages
    
    //a constructor method for the book class
    public Book(String title, int numberofPages){
        setTitle(title);
        setNumberofPages(numberofPages);
    }
    //a setter method that assigns the given title to title
    public void setTitle(String title){
        this.title = title;
    }
    //a getter method for the book title
    public String getTitle(){
        return this.title;
    }
    //a setter method for the number of pages in the book
    public void setNumberofPages(int numberofPages){
        if(numberofPages > 0){//check for a positve page number count
            this.numberofPages = numberofPages;
        }else{
            System.out.println("Page count cannot be 0 or negative");
        }
    }
    //a getter method that returns the number of pages in the provided book
    public int getNumberofPages(){
        return this.numberofPages;
    }
    
    
}//end of class

// code to test if the Book class works
/*class BookMaker{
    //the book maker class is used to create objects in the book class
    public static void main(String[] args){
        //create a book object
        Book book = new Book("Of Mice and Men", 428);
        
        //output the customers name, credit score, and rating
        System.out.println("Name: " + book.getTitle());
        System.out.println("Number of Pages: " + book.getNumberofPages());
    }
}*/