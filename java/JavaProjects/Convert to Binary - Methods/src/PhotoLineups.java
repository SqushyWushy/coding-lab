import java.util.Scanner;
import java.util.ArrayList;

public class PhotoLineups {

    // TODO: Write method to create and output all permutations of the list of names.
    public static void printAllPermutations(ArrayList<String> permList, ArrayList<String> nameList) {
        // Base case: if nameList is empty, print the current permutation
        if(nameList.size() == 0){
            // Print the current permutation
            for(int i = 0; i < permList.size();i++){
                if(i == permList.size()-1){
                    System.out.print(permList.get(i));
                }else{
                    System.out.print(permList.get(i) + ", ");
                }
            }
            System.out.println();
        }else{
            // Recursive case: generate permutations
            for(int i = 0; i < nameList.size();i++){
                ArrayList<String> newNameList = new ArrayList<String>(nameList);
                ArrayList<String> newPermList = new ArrayList<String>(permList);
                newPermList.add(newNameList.remove(i));
                printAllPermutations(newPermList, newNameList);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        ArrayList<String> nameList = new ArrayList<String>();
        ArrayList<String> permList = new ArrayList<String>();
        String name;

        name = scnr.next();
        while (!name.equals("-1")){
            nameList.add(name);
            name = scnr.next();
        }

        printAllPermutations(permList,nameList);
    }
}
