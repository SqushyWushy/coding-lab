/*
 * Jr Hector Gonzalez
 * 02/25/24
 * JDK 18.0.2.1
 * Creating a class for customers with a name and credit score
 */
public class Customer {
    private String name = null;
    private int creditScore = 300;
    
    //constructor for the Customer class
    //it sets the name and credit score through the parameters provided
    public Customer(String name, int creditScore){
        setName(name);
        setCreditScore(creditScore);
    }
    //setter method for the name
    public void setName(String name){
        this.name = name;
    }
    //getter method for the name
    public String getName(){
        return this.name;
    }
    //setter method for the credit score
    public void setCreditScore(int creditScore){
        if(creditScore < 300){
            this.creditScore = 300;//if the score is less than 300, set it to 300
        }else{
            this.creditScore = creditScore;// Otherwise , set the score to the provided value
        }
    }
    //getter method for the credit score
    public int getCreditScore(){
        return this.creditScore;
    }
    //method that returns the rating of the credit score
    public String getCreditRating(){
        if (this.creditScore >= 720){
            return "Excellent";
        }else if(this.creditScore >= 690){
            return "Good";
        }else if(this.creditScore >= 630){
            return "Fair";
        }else{
            return "Bad";// If the score does not fall into any of the above categories,
            //it will be considered bad.
        }
    }
}//end of class

//the customer class is used to create Customer objects and demonstrate their behavior
class CustomerCreator{
    public static void main(String[] args){
        //create a customer object with a name and credit score
        Customer customer = new Customer("Hector Gonzalez", 728);
        
        //output the customers name, credit score, and rating
        System.out.println("Name: " + customer.getName());
        System.out.println("Credit Score: " + customer.getCreditScore());
        System.out.println("Credit Rating: " + customer.getCreditRating());
    }
}//end of class
