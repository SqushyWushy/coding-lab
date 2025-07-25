# **Date: July 22nd, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

### Overview of the Strategy Pattern

This lecture focuses on the Strategy design pattern, which helps solve the problem of redundant code in subclasses that differ only in a single function. The pattern involves extracting varying behavior into separate "strategy" classes, allowing the main class to delegate specific behaviors rather than implementing them directly. The example used throughout is calculating capital for different types of loans, where the calculation varies based on factors like whether the loan is for veterans, elderly people, or education purposes.

### Problems Addressed by the Strategy Pattern

- Multiple subclasses that are identical except for one function (calculating capital)
- Redundant code that leads to maintenance issues
- Difficulty isolating changes when adding new functionality
- Code that mixes decision logic with implementation details

### Implementation Steps

- [ ] Create a parent Strategy class (e.g., CapitalStrategy)
- [ ] Move the varying method (capital calculation) from the main class to the Strategy class
- [ ] Modify the main class to delegate to the Strategy instead of performing the calculation
- [ ] Add a reference to the Strategy in the main class
- [ ] Create concrete Strategy subclasses for different calculation methods

### Benefits of the Strategy Pattern

- Isolates changes so you only need to modify specific strategy classes
- Separates concerns between what to do and how to do it
- Makes code more maintainable when adding new functionality
- Reduces redundancy and duplication
- Makes it easier to explain specific implementations to auditors or reviewers
- Preserves the interface of the main class while allowing for behavior variation

### Application to Homework

The lecturer referenced a previous homework assignment involving movie rentals, suggesting that the Strategy pattern could have been applied there:

- Different movie types (regular, children's, new release) had different price calculations
- The conditional logic used to calculate prices based on movie type could be refactored using the Strategy pattern
- This would improve code quality by separating the price calculation strategies from the rental logic

---

## **What we covered in the second hour**

---

### Key Concepts of the Strategy Pattern

- The Strategy pattern should be applied when specific conditions are met:
  1. One function with multiple variations and conditional logic
  2. Creating subclasses would lead to unnecessary code duplication
  3. The strategy selection is determined before code execution (at "static time")
  4. Every class must have one strategy (even if it's a default strategy)

### Strategy vs Decorator Patterns

- **Key Difference**: Strategy pattern decisions are made at static time, while Decorator pattern decisions are made at runtime
- Strategy pattern requires selecting exactly one strategy
- Decorator pattern allows for stacking multiple decorators or having none

### Real-World Examples

- **Strategy Examples**:
  - Movie rental pricing based on movie categories
  - Tariffs on products from different countries
  - Amazon Prime member pricing (fixed based on membership status)
  - Club membership privileges
- **Decorator Examples**:
  - Coupon codes for online purchases (can be applied/removed dynamically)
  - Text highlighting in documents (can be added/removed at runtime)

### Homework Modifications

- Students need to modify their existing code to implement the Strategy pattern
- Focus on implementing a function to compute random price
- The modification relates to rental/movie rental system pricing strategies
- New release movies should be handled as a strategy rather than a subclass

### Action Items

- [ ] Modify homework to implement the Strategy pattern for computing random price function
- [ ] Draw the design on paper showing what classes will be created
- [ ] Discuss implementation approach with classmates
