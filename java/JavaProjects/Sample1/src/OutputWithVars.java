import java.util.Scanner;

public class OutputWithVars {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int userNum;

        System.out.println("Enter integer:");
        userNum = scnr.nextInt();
        int squaredUserNum = userNum * userNum;
        int cubedUserNum = userNum * userNum * userNum;

        System.out.println("You entered: " + userNum);
        System.out.println(userNum + " squared is " + squaredUserNum);
        System.out.println("And " + userNum + " cubed is " + cubedUserNum + "!!");

        System.out.println("Enter  another integer:");
        int userNum1 = scnr.nextInt();
        int userNumSum = userNum + userNum1;
        int userNumMult = userNum * userNum1;

        System.out.println(userNum + " + " + userNum1 + " is " + userNumSum);
        System.out.println(userNum + " * " + userNum1 + " is " + userNumMult);
    }
}