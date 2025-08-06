public class Main {
    public static void main(String[] args) {
        Movie m1 = new Movie("Inception", new RegularMovieStrategy());
        Movie m2 = new Movie("Frozen", new ChildrenMovieStrategy());
        Movie m3 = new Movie("Oppenheimer", new NewReleaseMovieStrategy());

        Rental r1 = new Rental(m1, 3); // Regular, 3 days
        Rental r2 = new Rental(m2, 4); // Children, 4 days
        Rental r3 = new Rental(m3, 2); // New release, 2 days

        Customer customer = new Customer("Hector");
        customer.addRental(r1);
        customer.addRental(r2);
        customer.addRental(r3);

        System.out.println(customer.statement());
    }
}
