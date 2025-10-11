# CS 3354 – Assignment 4: Strategy & Decorator Patterns (Coupon System)

Written by Hector Gonzalez - Summer 2025 CS 3354 Assignment 4

## Overview

This project builds off my previous movie rental application and adds a coupon and reward system using design patterns. I used the Decorator Pattern to apply different types of discounts to individual rentals, and added logic in `Customer.java` to handle things like frequent renter points and transaction-level discounts.

Everything still builds off the Strategy Pattern setup I already had for rental pricing and point calculation.

---

## Features Implemented

### 1. 50% Off Coupon (Decorator)

I added a `HalfOffCoupon` decorator that wraps any rental and cuts the price in half.

```java
Rental rental = new HalfOffCoupon(new Rental(movie, 5));
```

### 2. $1 Off If Rental > $5 (Decorator)

I added a `OneDollarOffOverFiveCoupon` decorator that checks if the rental charge is over $5, and subtracts $1 if true.

```java
Rental rental = new OneDollarOffOverFiveCoupon(new Rental(movie, 4));
```

### 3. 10 Frequent Renter Points = Free Rental

In `Customer.statement()`, if the customer earns 10 or more points in a single transaction, I apply a `FreeRentalDecorator` to one of their rentals — making it free.

```java
if (frequentRenterPoints >= 10) {
    rentals.set(0, new FreeRentalDecorator(rentals.get(0)));
}
```

### 4. $5 Off If Customer Rents 5+ Movies

I also check how many rentals the customer has. If it’s 5 or more, I take $5 off the total.

```java
if (rentals.size() >= 5) {
    totalAmount -= 5;
}
```

---

## Design Patterns Used

- Strategy Pattern: Same as last time. Each `Movie` is given a `MoviePricingStrategy` like `RegularMovieStrategy`, `NewReleaseMovieStrategy`, or `ChildrenMovieStrategy`, which calculates the charge and renter points.

- Decorator Pattern: Used to apply coupons like `HalfOffCoupon` and `OneDollarOffOverFiveCoupon` without changing the original rental logic. This makes the code more flexible and easier to extend.

---

## How to Test

You can run everything by compiling and running `Main.java`. I made a test case that covers all the new features:

- One rental has 50% off
- Another has $1 off because it’s over $5
- The customer gets 10 or more frequent renter points, so one rental is free
- There are 5 or more rentals total, so $5 gets knocked off at the end

To run it:

```bash
javac *.java
java Main
```

Check the terminal output — it shows all the discounts and reward logic working as expected.

---

## Final Thoughts

This assignment made me think more about how to keep code clean while adding new features. It was helpful to see how well the Decorator Pattern worked for this problem. It made the logic easier to manage and test, and it kept things more organized than trying to cram everything into a few big methods like in earlier assignments.
