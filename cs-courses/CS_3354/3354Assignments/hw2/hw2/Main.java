// ===== Main.java (test program) =====
public class Main {

    public static void main(String[] args) {
        Movie matrix = new Movie("The Matrix", MovieType.REGULAR);
        Movie avengers = new Movie("Avengers: Endgame", MovieType.NEW_RELEASE);
        Movie nemo = new Movie("Finding Nemo", MovieType.CHILDRENS);

        Rental r1 = new Rental(matrix, 3);
        Rental r2 = new Rental(avengers, 2);
        Rental r3 = new Rental(nemo, 5);

        Customer john = new Customer("John Smith");
        john.addRental(r1);
        john.addRental(r2);
        john.addRental(r3);

        System.out.println(john.statement());
        System.out.println("\n--- XML OUTPUT ---\n");
        System.out.println(john.statementXml());
    }
}
