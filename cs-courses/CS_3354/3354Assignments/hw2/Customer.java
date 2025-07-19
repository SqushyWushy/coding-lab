// ===== Customer.java =====
import java.util.*;

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

    public List<Rental> getRentals() {
        return rentals;
    }

    public double getTotalCharge() {
        double total = 0;
        for (Rental rental : rentals) {
            total += rental.getCharge();
        }
        return total;
    }

    public int getTotalFrequentRenterPoints() {
        int total = 0;
        for (Rental rental : rentals) {
            total += rental.getFrequentRenterPoints();
        }
        return total;
    }

    public String statement() {
        return StatementFormatter.formatText(this);
    }

    public String statementXml() {
        return StatementFormatter.formatXml(this);
    }
}
