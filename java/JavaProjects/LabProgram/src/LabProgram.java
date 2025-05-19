import java.util.Scanner;

public class LabProgram {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int highwayNumber;
        int primaryNumber;


        System.out.println("Enter the highway number: ");
        highwayNumber = scnr.nextInt();
        String direction = (highwayNumber % 2 ==0) ? "east/west." : "north/south.";

        if(highwayNumber < 1 || highwayNumber > 999){
            System.out.println(highwayNumber + " is not a valid interstate highway number.");
        }else if(highwayNumber >= 1 && highwayNumber <= 99){
            System.out.println("I-" + highwayNumber + " is primary, going " + direction);
        }else{
            primaryNumber = highwayNumber % 100;

            if(primaryNumber == 0){
                System.out.println(highwayNumber + " is not a valid interstate highway number.");
            }else{
                System.out.println("I-" + highwayNumber + " is auxiliary, serving " + "I-" + primaryNumber +", going "
                        + direction);
            }
        }

    }
}