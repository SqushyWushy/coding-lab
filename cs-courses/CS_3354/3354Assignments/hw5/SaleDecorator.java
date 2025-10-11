// Lets you apply coupon logic to sales, like buy 2 get 1 free.
// It wraps around the Sale class so we don’t mess with its original logic.

public abstract class SaleDecorator extends Sale {

    protected Sale baseSale;

    public SaleDecorator(Sale baseSale) {
        super(baseSale.getMovie(), baseSale.getQuantityOrDays());
        this.baseSale = baseSale;
    }

    @Override
    public double getCharge() {
        return baseSale.getCharge();
    }

    @Override
    public int getFrequentRenterPoints() {
        return baseSale.getFrequentRenterPoints();
    }
}
