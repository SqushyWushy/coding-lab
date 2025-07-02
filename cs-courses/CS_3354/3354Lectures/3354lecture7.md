# **Date: July 1st, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

# _Code Smells and Refactoring Discussion_

This transcript covers a classroom discussion about identifying and fixing code smells in what appears to be a movie rental application. The instructor reviews code examples with students, highlighting various design issues and discussing refactoring techniques.

### Key Code Smells Identified

- **Feature Envy**: Methods that use data from other classes extensively (e.g., rental price calculation in customer class that should be in the rental class)
- **Switch Statements**: Multiple switch cases on the same condition (movie type) in different places
- **Magic Numbers**: Unexplained numeric literals (like 1.5, 2, 3) that lack descriptive names
- **Message Chains**: Navigating through multiple objects to get information (e.g., rental → movie → price code)
- **Duplicate Logic**: Similar patterns repeated across cases (e.g., pricing formulas for different movie types)
- **Missing Default Case**: Switch statement without a default handler for invalid input
- **Poor Variable Names**: Confusing identifiers with underscores
- **Recalculation**: Computing values repeatedly instead of storing them

### Refactoring Solutions

- Extract methods to improve code organization
- Move methods to appropriate classes (where the data they use is located)
- Replace conditional logic with polymorphism using superclasses and subclasses
- Use named constants instead of magic numbers
- Store computed values rather than recalculating them
- Add defensive programming checks (e.g., null checks)

### Homework Instructions

- **Homework 1**: Identify code smells and explain why they reduce maintainability
- **Homework 2**: Implement fixes for the identified code smells
- Submission format should include the smell name, the problematic code snippet, and explanation of the issue
- Deadline has been extended until Thursday

### Practical Advice

- In industry, explaining the maintenance cost of code smells is crucial to get approval for refactoring
- The "three strikes rule" - only after a problem appears three times is refactoring typically approved
- Good design reduces the amount of code that needs to be changed when adding new features

---

## **What we covered in the second hour:**

---

# _Code Refactoring Assignment Instructions for Homework 2_

This meeting covered instructions for an upcoming programming assignment (Homework 2) that focuses on code refactoring principles and implementation.

### Assignment Overview

- Homework 2 will require students to refactor code while implementing new functionality
- The assignment will count as a project with a higher score than Homework 1
- The purpose is to restructure code properly, not just fix identified code smells
- The assignment hasn't been posted yet as students are still completing Homework 1

### Requirements

- Create two new functions through refactoring
- Add a main method to test the program
- Create a new print statement with tags before and after name and movie
- Simply copying and modifying the print method will result in zero points

### Refactoring Approach

- Start by examining the customer class first
- Begin with local refactoring (extracting methods)
- Next, consider where to move the extracted code
- Create three new classes to improve the design
- Ensure the code doesn't break during each refactoring step

### Design Considerations

- Students should draw diagrams before writing code
- Two possible approaches:
  - Create three subclasses of Movie (Children movie, New release movie, and another type)
  - Alternative: create three subclasses of Rental
- Extracted methods should be moved to the appropriate classes

### Action Items

- [ ] Students to discuss design of new classes with lab partners
- [ ] Students to draw diagrams showing planned code refactoring
- [ ] Students to plan code extraction and function relocation
- [ ] Instructor to post Homework 2 assignment details
