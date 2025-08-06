## Assignment 3 - Strategy Pattern Implementation

For this assignment, we used the **Strategy Design Pattern** to handle two things:

1. How rental prices are calculated
2. How frequent renter points are awarded

Instead of keeping that logic in `Customer` or `Rental` (which gets messy fast), we created a group of strategy classes:

- `RegularMovieStrategy`
- `NewReleaseMovieStrategy`
- `ChildrenMovieStrategy`

Each one has its own logic for calculating charges and points. Then in the `Movie` class, we give each movie the right strategy and let it handle the work.

So now when something needs the rental cost or points, the movie just asks its strategy. This keeps everything cleaner and makes it easier to add new movie types in the future without touching the rest of the system.

No more giant switch statements — just clean, modular behavior.
