package monthcreator;

public class Month {
    private int monthNumber;//private field that stores the month number and its
    //private to ensure it can only be accessed and modified through the methods
    //of this class
    
    //create a constructor
    public Month(int m){
    if (m < 1 || m > 12){
        this.monthNumber = 1;
    }else{
        this.monthNumber = m;
    }
}
    public void setMonthNumber(int m){
    if (m < 1 || m > 12){
        this.monthNumber = 1;
    }else{
        this.monthNumber = m;
    }
}
    public int getMonthNumber(){
        return this.monthNumber;
    }
    public String getMonthName(){
        String[] monthNames = {
            "January", "February", "March", "April", "May", "June", "July", "August",
            "September", "October", "November", "December"};
        return monthNames[this.monthNumber-1];
    }
    public String getSeason(){
        if(this.monthNumber == 12 || this.monthNumber == 1 || this.monthNumber == 2){
            return "Winter";
        }else if(this.monthNumber >= 3 && this.monthNumber <= 5){
            return "Spring";
        }else if(this.monthNumber >= 6 && this.monthNumber <= 8){
            return "Summer";
        }else{
            return "Fall";
        }
    }
    @Override
    public String toString(){//Method to return a string representation of the month object
        return "Month number: " + this.getMonthNumber() + "\n" + 
                "Month name: " + this.getMonthName() + "\n" +
                "Month season: " + this.getSeason();
    }
    public boolean equals(Month month2){
        return this.monthNumber == month2.monthNumber;
    }
}
