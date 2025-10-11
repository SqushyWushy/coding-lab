// Now supports both rentals and purchases in the same statement.
// If you’ve got 10+ points, it’ll make one rental free.
// If you made 5 or more transactions, it knocks $5 off the total.

import java.util.ArrayList;
import java.util.List;

public class Customer {

    private String name;
    private List<Transaction> transactions = new ArrayList<>();

    public Customer(String name) {
        this.name = name;
    }

    public void addTransaction(Transaction transaction) {
        transactions.add(transaction);
    }

    public String getName() {
        return name;
    }

    public String statement() {
        double totalAmount = 0;
        int frequentRenterPoints = 0;
        StringBuilder result = new StringBuilder(
            "Rental/Sales Record for " + getName() + "\n"
        );

        for (Transaction transaction : transactions) {
            frequentRenterPoints += transaction.getFrequentRenterPoints();
        }

        // Apply free rental if points >= 10 (and transaction is rental)
        if (frequentRenterPoints >= 10) {
            for (int i = 0; i < transactions.size(); i++) {
                if (transactions.get(i) instanceof Rental) {
                    transactions.set(
                        i,
                        new FreeRentalDecorator((Rental) transactions.get(i))
                    );
                    result
                        .append("[Free Rental Applied to: ")
                        .append(transactions.get(i).getMovie().getTitle())
                        .append("]\n");
                    break;
                }
            }
        }

        for (Transaction transaction : transactions) {
            double thisAmount = transaction.getCharge();
            result
                .append("\t")
                .append(transaction.getMovie().getTitle())
                .append(" - ")
                .append(transaction instanceof Sale ? "Sale" : "Rental")
                .append("\t")
                .append(thisAmount)
                .append("\n");
            totalAmount += thisAmount;
        }

        if (transactions.size() >= 5) {
            totalAmount -= 5;
            result.append("$5 off applied for 5 or more transactions\n");
        }

        result.append("Amount owed is ").append(totalAmount).append("\n");
        result
            .append("You earned ")
            .append(frequentRenterPoints)
            .append(" frequent renter points");

        return result.toString();
    }
}
