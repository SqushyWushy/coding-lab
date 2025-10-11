// Just a test run to show everything working.
// Adds a bunch of rentals and sales with different coupons and prints out the full breakdown.

public class Main {

    public static void main(String[] args) {
        Movie regular = new Movie("Inception", new RegularMovieStrategy());
        Movie children = new Movie("Frozen", new ChildrenMovieStrategy());
        Movie newRelease = new Movie(
            "Oppenheimer",
            new NewReleaseMovieStrategy()
        );

        Customer customer = new Customer("Hector");

        // Rentals
        customer.addTransaction(new HalfOffCoupon(new Rental(regular, 5)));
        customer.addTransaction(
            new OneDollarOffOverFiveCoupon(new Rental(newRelease, 4))
        );
        customer.addTransaction(new Rental(children, 6));
        customer.addTransaction(new Rental(newRelease, 3));
        customer.addTransaction(new Rental(regular, 4));
        customer.addTransaction(new Rental(newRelease, 2));

        // Sales
        customer.addTransaction(new Sale(newRelease, 2)); // Buying 2 copies of Oppenheimer
        customer.addTransaction(new Sale(children, 1)); // Buying 1 Frozen

        System.out.println(customer.statement());
    }
}
