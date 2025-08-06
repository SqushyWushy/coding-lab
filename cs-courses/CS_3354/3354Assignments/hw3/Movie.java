public class Movie {

    private String title;
    private MoviePricingStrategy pricingStrategy;

    public Movie(String title, MoviePricingStrategy strategy) {
        this.title = title;
        this.pricingStrategy = strategy;
    }

    public String getTitle() {
        return title;
    }

    public double getCharge(int daysRented) {
        return pricingStrategy.getCharge(daysRented);
    }

    public int getFrequentRenterPoints(int daysRented) {
        return pricingStrategy.getFrequentRenterPoints(daysRented);
    }
}
//Strategy Pattern: delegates charge and point logic based on movie type
