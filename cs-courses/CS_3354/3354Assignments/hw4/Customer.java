import java.util.List;
import java.util.ArrayList;


public class Customer {
    private String name;
    private List<Rental> rentals = new ArrayList<>();

    public Customer(String name) {
        this.name = name;
    }

    public void addRental(Rental rental) {
        rentals.add(rental);
    }

    public String getName() {
        return name;
    }

    public String statement() {
        double totalAmount = 0;
        int frequentRenterPoints = 0;
        StringBuilder result = new StringBuilder("Rental Record for " + getName() + "\n");

        // Point tally first
        for (Rental rental : rentals) {
            frequentRenterPoints += rental.getFrequentRenterPoints();
        }

        // Apply free rental if points >= 10
        if (frequentRenterPoints >= 10 && !rentals.isEmpty()) {
            rentals.set(0, new FreeRentalDecorator(rentals.get(0)));
            result.append("[Free Rental Applied to: ").append(rentals.get(0).getMovie().getTitle()).append("]\n");
        }

        // Now calculate charges
        for (Rental rental : rentals) {
            double thisAmount = rental.getCharge();
            result.append("\t").append(rental.getMovie().getTitle()).append("\t").append(thisAmount).append("\n");
            totalAmount += thisAmount;
        }

        // Apply $5 off if 5+ rentals
        if (rentals.size() >= 5) {
            totalAmount -= 5;
            result.append("$5 off applied for 5 or more rentals\n");
        }

        result.append("Amount owed is ").append(totalAmount).append("\n");
        result.append("You earned ").append(frequentRenterPoints).append(" frequent renter points");

        return result.toString();
    }
}
