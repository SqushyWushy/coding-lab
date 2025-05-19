import java.util.Scanner;

public class LabProgram {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        boolean keepRunning = true;
        // Main loop that continues until the user inputs "done", "Done", or "d"
        while(keepRunning){
            String original = input.nextLine();
            String reverse = "";

            if(original.equals("done") || original.equals("Done") || original.equals("d")){
                keepRunning = false;
            }else {
                for (int i = original.length() - 1; i >= 0; i--) {
                    reverse += original.charAt(i);
                }
                System.out.println(reverse);
            }
        }
    }
}
