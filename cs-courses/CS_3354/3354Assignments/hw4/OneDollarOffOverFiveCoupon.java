public class OneDollarOffOverFiveCoupon extends RentalDecorator {
    public OneDollarOffOverFiveCoupon(Rental baseRental) {
        super(baseRental);
    }

    @Override
    public double getCharge() {
        double original = baseRental.getCharge();
        return (original > 5) ? original - 1 : original;
    }
}
