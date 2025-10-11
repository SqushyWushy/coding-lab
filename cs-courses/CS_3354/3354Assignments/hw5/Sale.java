// Represents buying a movie instead of renting it.
// Each copy costs $10, and you earn 1 point per movie bought.

public class Sale extends Transaction {

    private static final double SALE_PRICE_PER_UNIT = 10.0;

    public Sale(Movie movie, int quantity) {
        super(movie, quantity);
    }

    @Override
    public double getCharge() {
        return SALE_PRICE_PER_UNIT * quantityOrDays;
    }

    @Override
    public int getFrequentRenterPoints() {
        return quantityOrDays; // 1 point per movie sold
    }
}
