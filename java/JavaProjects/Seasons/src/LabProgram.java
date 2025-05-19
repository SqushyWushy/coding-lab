import java.util.Scanner;

public class LabProgram {

    public static String determineSeason(String month, int day) {
        if ((month.equals("March") && day >= 20) || month.equals("April") || month.equals("May") || (month.equals("June") && day <= 20)) {
            return "Spring";
        }
        else if ((month.equals("June") && day >= 21) || month.equals("July") || month.equals("August") || (month.equals("September") && day <= 21)) {
            return "Summer";
        }
        else if ((month.equals("September") && day >= 22) || month.equals("October") || month.equals("November") || (month.equals("December") && day <= 20)) {
            return "Autumn";
        }
        else if ((month.equals("December") && day >= 21) || month.equals("January") || month.equals("February") || (month.equals("March") && day <= 19)) {
            return "Winter";
        }
        else {
            return "Invalid";
        }
    }
    public static boolean isValidDate(String month, int day){
        switch (month){
            case "January": case "March": case "May": case "July":
            case "August": case "October": case "December":
                return day >= 1 && day <= 31;
            case "April": case "June": case "September": case "November":
                return day >= 1 && day <= 30;
            case "February":
                return day >= 1 && day <=29;
                //assuming leap year of course
            default:
                return false;
        }
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String inputMonth = scnr.next();
        int inputDay = scnr.nextInt();
        if(isValidDate(inputMonth,inputDay)){
            String season = determineSeason(inputMonth, inputDay);
            System.out.println(season);
        }else{
            System.out.println("Invalid");
        }
        scnr.close();
    }
}
