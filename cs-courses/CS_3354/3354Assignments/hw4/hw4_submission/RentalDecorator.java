public abstract class RentalDecorator extends Rental {
    protected Rental baseRental;

    public RentalDecorator(Rental baseRental) {
        super(baseRental.getMovie(), baseRental.getDaysRented());
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
