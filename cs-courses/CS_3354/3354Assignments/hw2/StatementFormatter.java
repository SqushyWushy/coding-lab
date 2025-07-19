// ===== StatementFormatter.java =====
public class StatementFormatter {

    public static String formatText(Customer customer) {
        StringBuilder result = new StringBuilder(
            "Rental Record for " + customer.getName() + "\n"
        );
        for (Rental rental : customer.getRentals()) {
            result.append(
                "\t" +
                rental.getMovie().getTitle() +
                "\t" +
                rental.getCharge() +
                "\n"
            );
        }
        result.append("Amount owed is " + customer.getTotalCharge() + "\n");
        result.append(
            "You earned " +
            customer.getTotalFrequentRenterPoints() +
            " frequent renter points"
        );
        return result.toString();
    }

    public static String formatXml(Customer customer) {
        StringBuilder result = new StringBuilder();
        result.append("<customer>\n");
        result.append("  <name>" + customer.getName() + "</name>\n");
        for (Rental rental : customer.getRentals()) {
            result.append("  <rental>\n");
            result.append(
                "    <movie>" + rental.getMovie().getTitle() + "</movie>\n"
            );
            result.append("    <days>" + rental.getDaysRented() + "</days>\n");
            result.append("    <charge>" + rental.getCharge() + "</charge>\n");
            result.append("  </rental>\n");
        }
        result.append(
            "  <totalCharge>" + customer.getTotalCharge() + "</totalCharge>\n"
        );
        result.append(
            "  <frequentRenterPoints>" +
            customer.getTotalFrequentRenterPoints() +
            "</frequentRenterPoints>\n"
        );
        result.append("</customer>");
        return result.toString();
    }
}
