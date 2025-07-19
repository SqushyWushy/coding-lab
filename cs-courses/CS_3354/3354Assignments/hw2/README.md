# Homework 2 – Refactoring Movie Rental

**Name:** Hector Gonzalez

**Teammates:** None

---

## What This Project Is About

The original movie rental system was pretty messy, lots of code jammed into the `Customer` class, magic numbers used for movie types, and no real separation of responsibilities. The goal of this refactor was to clean that up and make the code easier to read, test, and expand later.

---

## Refactor Changes I Made

### 1. Method Extraction

I pulled out a few chunks of logic and turned them into separate methods to make the code cleaner:

- `getCharge()` was moved into the `Movie` class to handle pricing for each movie type.
- `getFrequentRenterPoints()` was also moved to `Movie` so it’s not the customer’s job anymore.
- The formatting logic (both text and XML) was pulled into its own class called `StatementFormatter`.

### 2. New Classes Added

To organize things better, I added:

- `MovieType`, an `enum` to replace the old `int`-based price codes
- `StatementFormatter` — this handles output so `Customer` doesn’t have to
- `Main`, a basic test runner that creates sample data and prints results

### 3. Methods Moved

- `getCharge()` and `getFrequentRenterPoints()` used to be calculated by the customer, which didn’t make sense. Now they live in the `Movie` class.
- Output formatting now lives in `StatementFormatter` instead of cluttering up `Customer`.

### 4. Renamed for Clarity

- `getPriceCode()` became `getType()` since it now returns a `MovieType`, not an `int`
- `amountFor()` became `getCharge()` to make it super obvious what it does
- I also made `_rentals` generic (`Vector<Rental>`) to avoid warnings and clarify what it holds

### 5. Data Type Replacements

The old `int` for movie type (like `0`, `1`, `2`) was replaced with a `MovieType` enum. This makes the code easier to read and less prone to bugs.

---

## How to Test It

Run `Main.java`. It’ll create a customer with 3 movie rentals and print out both the plain text version and the XML version of the rental statement. This shows that the program still works and is now easier to extend or modify.

---

## Why This Refactor Helped

- Got rid of hard-to-understand code and “magic numbers”
- Made each class responsible for its own stuff (good object-oriented design)
- Easier to read, maintain, and update later (like adding new movie types or formats)

---

## Final Thoughts

This project really showed how small changes—like moving a method or renaming a variable, can make a big difference in how understandable your code is. It also made me appreciate enums way more than I used to.
