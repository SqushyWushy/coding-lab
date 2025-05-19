import java.util.ArrayList;
import java.util.Scanner;

public class LabProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        while (x > 0) {
            int remainder = x % 2;
            list.add(remainder);
            x = x / 2;
        }
        String binaryString = "";
        for(int i = 0; i < list.size(); i++){
            binaryString += list.get(i);
        }
        System.out.println(binaryString);
    }
}
