public class HalfOffCoupon extends RentalDecorator {
    public HalfOffCoupon(Rental baseRental) {
        super(baseRental);
    }

    @Override
    public double getCharge() {
        return baseRental.getCharge() * 0.5;
    }
}
