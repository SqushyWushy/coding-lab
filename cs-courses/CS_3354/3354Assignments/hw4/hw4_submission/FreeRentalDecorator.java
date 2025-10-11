public class FreeRentalDecorator extends RentalDecorator {
    public FreeRentalDecorator(Rental baseRental) {
        super(baseRental);
    }

    @Override
    public double getCharge() {
        return 0;
    }
}
