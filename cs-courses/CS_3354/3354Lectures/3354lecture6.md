# **Date: June 24th, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

This lecture covered various refactoring techniques in object-oriented programming, focusing on how to improve code organization, maintainability, and testability.

### Key Refactoring Principles

The lecture emphasized high cohesion (each class having a single responsibility), reducing duplication, and decoupling components. These principles make code more maintainable, especially in large projects with thousands of lines of code.

### Extract Class Technique

The speaker demonstrated how to extract functionality from a class when it handles multiple concerns:

- Example: Separating phone functionality from a Customer class
- Benefits: Allows one customer instance to have multiple phone numbers
- Similar approach for addresses (billing vs shipping)

### Extract Method Technique

Breaking down large methods into smaller, more focused ones:

- Demonstrated with a printAccountDetails example that was separated into printSummary and printHistory
- While seemingly excessive for small projects, this approach becomes valuable in large codebases
- Makes testing easier as individual functionalities can be tested separately

### Class Hierarchy Techniques

Several approaches to organizing class hierarchies were covered:

1. **Extract Subclass**
   - Useful when a class has attributes only relevant to specific subtypes
   - Example: Moving jobTitle from Person to Employee subclass
   - Eliminates need for conditional checks in the parent class
2. **Extract Superclass**
   - Finding common attributes between classes and moving them to a parent class
   - Reduces duplication by centralizing shared functionality
   - Example: Creating a Person superclass for Student and Employee
3. **Template Methods**
   - Creating abstract structures in parent classes that subclasses implement
   - Particularly useful for large teams to ensure consistent implementation
   - Example: printNameAndDetails method implemented similarly across subclasses

### Additional Techniques

- **Move Method**: Relocating methods to the class where most of their data resides
- **Data Encapsulation**: Using private fields and accessor methods to protect data integrity

### Practical Considerations

- Code smells typically appear as software evolves, not in initial implementations
- Test-driven approach: ensure tests pass after refactoring
- Modern IDEs and tools (Eclipse, Visual Studio, VS Code) offer automated refactoring
- Caution with AI tools like ChatGPT for refactoring - always verify behavior preservation

### Action Items

- [ ] Take a 10-minute break
- [ ] Complete the refactoring quiz mentioned in the lecture
