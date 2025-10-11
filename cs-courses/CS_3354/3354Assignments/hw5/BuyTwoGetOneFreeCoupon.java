// If you’re buying 3 movies, you only pay for 2 of them.
// Automatically figures out how many are free based on the quantity.

public class BuyTwoGetOneFreeCoupon extends SaleDecorator {

    public BuyTwoGetOneFreeCoupon(Sale baseSale) {
        super(baseSale);
    }

    @Override
    public double getCharge() {
        int quantity = baseSale.getQuantityOrDays(); // since it's a sale
        int chargeable = quantity - (quantity / 3); // every 3rd is free
        return baseSale.getMovie().getCharge(0) * chargeable;
    }
}
