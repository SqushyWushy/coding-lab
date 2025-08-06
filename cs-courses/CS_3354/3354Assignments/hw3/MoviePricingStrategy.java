// Strategy Interface for pricing and frequent renter points
public abstract class MoviePricingStrategy {
    public abstract double getCharge(int daysRented);

    public int getFrequentRenterPoints(int daysRented) {
        return 1;
    }
}
