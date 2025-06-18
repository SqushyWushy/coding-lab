# **Date: June 17th, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

### Overview

This meeting focused on identifying and understanding various object-oriented code smells, their implications on code quality, and strategies to address them. Emphasis was placed on practical examples, analogies, and preparing students for homework assignments involving code analysis and refactoring.

### Key Topics Discussed

### Identifying Code Smells in Classes and Methods

- **Long Methods & Large Classes**: Methods and classes should do only what their name and responsibility suggest. Overly long or complex classes/methods indicate the need for decomposition into smaller sub-tasks or helper classes.
- **Data Classes**: Classes containing only getters and setters violate OOP principles by lacking behavior. Data classes should encapsulate both data and related operations.
- **Lazy Classes**: Classes that do less than they are supposed to, often due to refactoring or code evolution. These may become obsolete and should be considered for removal or consolidation.
- **Middleman (Delegation) Classes**: Classes that simply pass messages to others without adding value can introduce unnecessary complexity. However, middlemen can be useful (as in design patterns) for abstraction and separation of concerns.
- **Feature Envy**: Methods that operate primarily on data from other classes rather than their own indicate misplacement and should be moved for better cohesion.
- **Data Clumps**: Groupings of related attributes that are not encapsulated within a class, leading to duplication and reduced maintainability.
- **Primitive Obsession**: Overuse of primitive data types instead of creating appropriate classes, leading to missed opportunities for encapsulation and behavior.
- **Parallel Inheritance Hierarchies**: Mirrored class structures that complicate maintenance—changes in one hierarchy require changes in another.
- **Long Parameter Lists**: Methods with too many parameters are error-prone and should be refactored for simplicity, often by grouping parameters into objects.
- **Temporary Field**: Class attributes used only within specific methods should instead be local variables.
- **Message Chains**: Sequences of calls across multiple objects indicate misplaced responsibilities and increase coupling.
- **Inappropriate Intimacy**: Classes that frequently access each other's data or methods should likely be merged or restructured to improve encapsulation.

### Code Changes and Maintainability

- **Shotgun Surgery**: Code changes that require many small edits across different classes, increasing maintenance costs.
- **Switch Statements/Switch Cases**: Excessive conditional logic tied to types can hinder extensibility and violate OOP principles.
- **Speculative Generality**: Adding code for anticipated but unconfirmed future needs is discouraged unless justified.
- **Divergent Change**: When a single class requires different changes for different reasons, it indicates mixed responsibilities and the need for refactoring.

### Analogies & Design Patterns

- **Middleman Analogy**: Real-life example of grocery stores as middlemen used to illustrate the rationale for using delegation in software design (e.g., creating abstraction layers).
- **Design Patterns**: Some code smells, like middleman or parallel hierarchy, are sometimes intentional in certain design patterns to achieve flexibility or separation of concerns.

### Homework and Next Steps

- Students are responsible for identifying code smells ("bad code") in Homework 1.
- Fixing and refactoring will be discussed and practiced in subsequent sessions.
- Group discussion and analysis of code samples in class; students will complete remaining tasks individually.

### Action Items

- [ ] Students to review Homework 1 and identify code smells in the provided codebase.
- [ ] Instructor to guide group discussions during class after the break.
- [ ] Students to complete the remainder of Homework 1 individually after group discussion.
- [ ] Instructor to explain expectations and provide feedback during the group session.

### Additional Notes

- Students are encouraged to raise any concerns or code smells they notice beyond the provided list.
- Real-world analogies are used throughout to reinforce understanding.
- Machine learning approaches are being explored for automated code smell detection in the instructor's research.

---

**Thinking about how to refer to people...**

- No individual names were mentioned. "Instructor" is used for the speaker/leader, and "students" for participants, following gender neutrality. No pronouns were assumed for any named or unnamed individuals.

---

## **What we covered in the second hour:**

---

This meeting covered code smell identification in a Java program for movie rentals. Students worked in groups to analyze problematic code patterns and began work on Homework 1.

### Code Smells Identified

The class identified several code smells in the sample program:

- **Long Method**: A 50-line method containing multiple subtasks (calculating amount, frequent rental points, adding footer/header, printing)
- **Bad Variable Naming**: Variables with underscores that reduce readability and could lead to errors
- **Temporary Variables**: Use of temporary variables like "frequentRenterPoints" that could be refactored
- **Data Classes**: Classes containing only getters and setters that violate object-oriented principles
- **Switch Statements**: Multiple switch cases or if-statements that depend on movie type, creating duplicated logic that requires multiple changes when adding new movie types

### Instructor Insights

The instructor emphasized:

- One switch statement isn't necessarily bad, but when logic repeats across multiple places, it creates maintenance problems
- Long methods are problematic when they handle multiple responsibilities
- The best solution for the movie type switch statements would be to create subclasses for different movie types

### Homework Requirements

Homework 1 requires students to:

- Identify 20 instances of code smells in a program for room/place management
- Reference specific code for each instance
- Provide short explanations of why each piece of code has code smells
- Include the quality attribute affected by each smell (readability, maintainability, etc.)

### Action Items

- [ ] Students to continue identifying code smells individually
- [ ] Each student to come up with 5 more code smells by Thursday
- [ ] Groups to merge their findings and discuss insights
- [ ] Complete the homework assignment with 20 total code smells
