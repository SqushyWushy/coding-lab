// Works just like the sale one but for rentals.
// Lets you plug in coupons like half off or $1 off without touching the rental logic directly.

public abstract class RentalDecorator extends Transaction {

    protected Rental baseRental;

    public RentalDecorator(Rental baseRental) {
        super(baseRental.getMovie(), baseRental.getQuantityOrDays());
        this.baseRental = baseRental;
    }

    @Override
    public double getCharge() {
        return baseRental.getCharge();
    }

    @Override
    public int getFrequentRenterPoints() {
        return baseRental.getFrequentRenterPoints();
    }
}
