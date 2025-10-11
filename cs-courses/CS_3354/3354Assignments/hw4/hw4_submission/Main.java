// This test case shows all four features: two coupon decorators,
// the frequent renter point reward, and the $5 off for 5+ rentals.
// Written by Hector Gonzalez - Summer 2025 CS 3354 Assignment 4

public class Main {

    public static void main(String[] args) {
        // define movie strategies
        Movie regularMovie = new Movie("Inception", new RegularMovieStrategy());
        Movie childrensMovie = new Movie("Frozen", new ChildrenMovieStrategy());
        Movie newReleaseMovie = new Movie(
            "Oppenheimer",
            new NewReleaseMovieStrategy()
        );

        // rentals using different coupons and strategies

        // 50% off on Regular
        Rental rental1 = new HalfOffCoupon(new Rental(regularMovie, 5)); // Regular (~5.0) → 2.5

        // $1 off if over $5
        Rental rental2 = new OneDollarOffOverFiveCoupon(
            new Rental(newReleaseMovie, 4)
        ); // New Release (12.0) → 11.0

        // normal Children’s rental
        Rental rental3 = new Rental(childrensMovie, 6); // Children (~6.0)

        // extra rentals to trigger 5+ rentals AND boost points
        Rental rental4 = new Rental(newReleaseMovie, 3); // 9.0 → 2 points
        Rental rental5 = new Rental(regularMovie, 4); // ~5.0 → 1 point
        Rental rental6 = new Rental(newReleaseMovie, 2); // 6.0 → 2 points

        //create customer and add rentals
        Customer customer = new Customer("Hector");
        customer.addRental(rental1);
        customer.addRental(rental2);
        customer.addRental(rental3);
        customer.addRental(rental4);
        customer.addRental(rental5);
        customer.addRental(rental6);

        // print statement (includes all discounts and logic)
        System.out.println(customer.statement());
    }
}
