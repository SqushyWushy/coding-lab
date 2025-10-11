// Used to add extra behavior (like coupons) to rentals or sales without changing their original code.
// This is the wrapper class that makes all the coupon stuff work cleanly.

public abstract class TransactionDecorator extends Transaction {

    protected Transaction baseTransaction;

    public TransactionDecorator(Transaction baseTransaction) {
        super(baseTransaction.getMovie(), baseTransaction.getQuantityOrDays());
        this.baseTransaction = baseTransaction;
    }

    @Override
    public double getCharge() {
        return baseTransaction.getCharge();
    }

    @Override
    public int getFrequentRenterPoints() {
        return baseTransaction.getFrequentRenterPoints();
    }
}
