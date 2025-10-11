public class Movie {
    private String title;
    private MoviePricingStrategy strategy;

    public Movie(String title, MoviePricingStrategy strategy) {
        this.title = title;
        this.strategy = strategy;
    }

    public String getTitle() {
        return title;
    }

    public double getCharge(int daysRented) {
        return strategy.getCharge(daysRented);
    }

    public int getFrequentRenterPoints(int daysRented) {
        return strategy.getFrequentRenterPoints(daysRented);
    }
}
