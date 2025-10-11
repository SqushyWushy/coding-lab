// Represents a rental, now treated as just one type of transaction.
// The number passed in is how many days the movie was rented for.

public class Rental extends Transaction {

    public Rental(Movie movie, int daysRented) {
        super(movie, daysRented);
    }

    @Override
    public double getCharge() {
        return movie.getCharge(quantityOrDays);
    }

    @Override
    public int getFrequentRenterPoints() {
        return movie.getFrequentRenterPoints(quantityOrDays);
    }
}
