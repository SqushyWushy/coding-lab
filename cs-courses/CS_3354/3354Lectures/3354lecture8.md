# **Date: July 10th, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

This lecture introduced object-oriented design patterns, focusing primarily on the Singleton pattern. The instructor provided context about design patterns and their importance in software architecture before diving into implementation details.

### Design Pattern Resources

The instructor recommended the "Gang of Four" design patterns book, mentioning a professional connection with author Brad Johnson, a former professor at URUC. They noted that while the original book contained 23 patterns, many more are now available online. The instructor plans to upload a two-page design pattern structure reference card for students to use.

### Understanding Design Patterns

Design patterns are structured approaches to organizing classes - not frameworks or libraries that can be imported. They define how classes:

- Communicate with each other
- Form hierarchies through inheritance
- Customize behavior
- Connect to form larger structures

The instructor highlighted three popular categories of design patterns:

- Creational patterns
- Structural patterns (how elements connect)
- Behavioral patterns (how elements interact after connection)

### The Singleton Pattern

The Singleton pattern ensures only one instance of a class exists within an application. This is useful for:

- Security concerns (detecting unauthorized access)
- Resource management
- Maintaining data integrity

The implementation involves:

- Making the constructor private to prevent direct instantiation
- Creating a static instance variable to hold the single instance
- Providing a public static method that checks if an instance exists and creates one if needed

The instructor used an analogy of controlling access through a locked door, where the getInstance() method acts as the gatekeeper that ensures only one instance is ever created.

### Action Items

- [ ] Read the recommended Gang of Four design patterns book
- [ ] Review the design pattern structure card that will be uploaded by the instructor
- [ ] Study the Singleton pattern implementation example from class
