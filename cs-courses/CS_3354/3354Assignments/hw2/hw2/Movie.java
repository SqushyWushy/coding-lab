// ===== Movie.java =====
public class Movie {

    private String title;
    private MovieType type;

    public Movie(String title, MovieType type) {
        this.title = title;
        this.type = type;
    }

    public MovieType getType() {
        return type;
    }

    public String getTitle() {
        return title;
    }

    public double getCharge(int daysRented) {
        switch (type) {
            case REGULAR:
                double result = 2;
                if (daysRented > 2) result += (daysRented - 2) * 1.5;
                return result;
            case NEW_RELEASE:
                return daysRented * 3;
            case CHILDRENS:
                result = 1.5;
                if (daysRented > 3) result += (daysRented - 3) * 1.5;
                return result;
        }
        return 0;
    }

    public int getFrequentRenterPoints(int daysRented) {
        return (type == MovieType.NEW_RELEASE && daysRented > 1) ? 2 : 1;
    }
}
