import java.util.Scanner;

// main class
public class ProductManager {

    // prints the menu
    private static void displayMenu() {
        System.out.println("\nOperations on List");
        System.out.println("1. Make Empty");
        System.out.println("2. Find ID");
        System.out.println("3. Insert At Front");
        System.out.println("4. Delete From Front");
        System.out.println("5. Delete ID");
        System.out.println("6. Print All Records");
        System.out.println("7. Done");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        GenericLinkedList<Product> productList = new GenericLinkedList<>();

        boolean running = true;

        while (running) {
            displayMenu();
            System.out.print("Your choice: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // eat the newline

            if (choice == 1) {
                // make empty
                productList.makeEmpty();
                System.out.println("List has been emptied.");

            } else if (choice == 2) {
                // find ID
                System.out.print("ID No: ");
                int searchID = scanner.nextInt();
                scanner.nextLine();

                Product foundProduct = productList.findID(searchID);
                if (foundProduct != null) {
                    foundProduct.printID();
                } else {
                    System.out.println("Product with ID " + searchID + " not found.");
                }

            } else if (choice == 3) {
                // insert at front
                System.out.print("Enter Product ID: ");
                int productID = scanner.nextInt();
                scanner.nextLine();

                System.out.print("Enter Product Name: ");
                String productName = scanner.nextLine();

                System.out.print("Enter Supplier Name: ");
                String supplierName = scanner.nextLine();

                Product newProduct = new Product(productID, productName, supplierName);

                if (productList.insertAtFront(newProduct)) {
                    System.out.println("Product Added");
                } else {
                    System.out.println("Product with ID " + productID + " already exists.");
                }

            } else if (choice == 4) {
                // delete from front
                Product deletedProduct = productList.deleteFromFront();
                if (deletedProduct != null) {
                    deletedProduct.printID();
                    System.out.println("First item deleted");
                } else {
                    System.out.println("List is empty. Nothing to delete.");
                }

            } else if (choice == 5) {
                // delete ID
                System.out.print("ID No: ");
                int deleteID = scanner.nextInt();
                scanner.nextLine();

                Product deletedByID = productList.delete(deleteID);
                if (deletedByID != null) {
                    deletedByID.printID();
                    System.out.println("Item deleted");
                } else {
                    System.out.println("Product with ID " + deleteID + " not found.");
                }

            } else if (choice == 6) {
                // print all
                productList.printAllRecords();

            } else if (choice == 7) {
                // done
                System.out.println("Done.");
                running = false;

            } else {
                System.out.println("Invalid choice. Please select a number between 1 and 7.");
            }
        }

        scanner.close();
    }
}
