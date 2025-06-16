# **Date: June 12th, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

---

This class session covered the course structure and introduced software design principles, focusing on what makes "beautiful code" and the importance of proper design.

### Course Structure

- Project-based assessment with no final exam or midterm
- Homework assignments will build throughout the semester into larger projects
- Group work allowed for projects
- 5% of grade allocated to attendance and participation
- In-class homework sessions to provide clear expectations
- No required textbooks - relevant materials will be shared as needed
- Students should bring laptops to class

### Beautiful Code Properties

- Optimized and efficient
- Easy to read and understand
- No duplicated logic (using utility functions instead)
- Maintainable and testable
- Scalable for future growth
- Adaptable to new environments
- Reusable across projects

### AI and Code Generation

- Current AI can write functions/classes but struggles with entire projects
- Large language models often memorize code rather than understand design principles
- The professor conducts research on teaching AI to understand code abstraction
- Students may use LLM tools but should understand their limitations
- Models performed well in lab settings but poorly on new, unseen projects

### Software Development Challenges

- Requirements are often unclear, conflicting, or changing
- Code maintenance consumes significant resources:
  - 20% on corrective maintenance
  - 20% on adapting to different environments
  - 50% on adding functionality

### Design Principles

- Separation of concerns is the fundamental principle
  - Keep features and concerns isolated from each other
  - Changes in one area should minimally impact others
  - "Don't touch my code" philosophy from Microsoft
- Modularity helps achieve separation of concerns
- Abstraction allows handling complex systems at appropriate levels

This lecture focused on the principle of designing systems that can accommodate future changes while avoiding overengineering.

### Balancing Design Flexibility

- Design systems that can sustain change over time
- Find the fine line between anticipating reasonable future requirements and overengineering
- Avoid adding features just because they might be needed someday
- Be prepared to explain and justify design decisions that anticipate specific changes

### Management Perspective

- Management is concerned with efficiency and timelines
- They prefer focused effort that addresses current needs with reasonable flexibility
- Overengineering is viewed as wasting company resources and time

### Amazon Example

- Used Amazon's product system as an example for anticipating different types of prices
- Discussed how Amazon has expanded from simple product sales to include rentals and AWS computing services
- Shows how a good design would accommodate these evolving business models

### Action Items

- [ ] Complete the homework assignment involving Amazon-like pricing models
- [ ] Students to access e-learning for lecture notes and homework
- [ ] Students to enable homework notifications in e-learning if desired
- [ ] Students to bring laptops to class for in-class work

---

## **What we covered in the second hour:**

---

This session covered software quality principles and how to identify problematic code patterns ("code smells").

### Software Quality Categories

Software quality can be viewed from multiple perspectives:

- External quality: visible to users (performance, efficiency, scalability)
- Internal quality: important for developers (maintainability, readability)
- Product quality vs. process quality

### Key Quality Attributes

- **Correctness**: An absolute property - software either works correctly or doesn't, based on requirements
- **Reliability**: Statistical property - how consistently software works correctly over time (especially critical for systems like car brakes)
- **Robustness**: Ability to handle unforeseen or extreme situations (like autonomous vehicles encountering unexpected scenarios)
- **Usability**: Whether the software can be effectively used
- **Understandability**: Subjective property including code readability, logical organization, and appropriate comments
- **Verification**: Formal proving of software correctness (for mission-critical systems)
- **Maintainability**: General term covering ease of maintenance, including:
  - Evolvability: Adding new features
  - Portability: Working across different environments
  - Adaptability: Adjusting to new requirements
- **Reusability**: Ability to construct new components from existing ones
- **Scalability**: Not just handling larger inputs but doing so efficiently (linear vs. exponential response)

### Mission-Critical Software

- Requires formal verification before implementation
- Examples include missile control systems, nuclear control, and autonomous vehicles
- May require extensive proofs (speaker mentioned creating a 300-page proof for defense contract software)

### Code Smells

The session began covering "code smells" - correctly functioning code with design problems:

- **Duplicated Code**:
  - Violates maintainability
  - When bugs are fixed in one location but not in duplicated sections
  - Story shared about a tool that detected duplicated code revealing unfixed bugs
- **Long Methods**:
  - Hard to read and understand
  - Length should depend on purpose rather than arbitrary line counts
  - Methods should do only what their name indicates
