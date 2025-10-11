// Base class for both rentals and sales.
// It stores the movie and how many days/units the transaction involves.
// Any class that extends this has to say how much it costs and how many points it gives.

public abstract class Transaction {

    protected Movie movie;
    protected int quantityOrDays;

    public Transaction(Movie movie, int quantityOrDays) {
        this.movie = movie;
        this.quantityOrDays = quantityOrDays;
    }

    public Movie getMovie() {
        return movie;
    }

    public int getQuantityOrDays() {
        return quantityOrDays;
    }

    public abstract double getCharge();

    public abstract int getFrequentRenterPoints();
}
