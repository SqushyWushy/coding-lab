# **Date: June 5th, 2025 -- Software Engineering**

---

## **What did we cover in the first hour?**

---

This lecture discusses different software development process models, their characteristics, and appropriate use cases, emphasizing the trade-offs between quality, speed, and flexibility.

### Waterfall Model

- Highly sequential, mission-critical approach with distinct phases
- Used when human cost of failure is high (NASA space shuttle example: 400,000 lines of code with only one bug)
- Requirements are extremely detailed (26,000+ pages)
- Major drawback: very slow to adapt to changing requirements
- Can take years to complete a single cycle

### Iterative Model

- Combines "weak cycles" where iterations build upon each other
- More flexible than waterfall, allowing for requirement changes between iterations
- Accepts that iterations might fail but provides faster feedback
- Example: Apache Ant project developed a prototype in one month, stable version in six months
- Best for day-to-day applications where time-to-market matters
- Analogy: writing and editing chapter-by-chapter vs. completing entire novel before editing

### Prototype Model

- Used when requirements are unclear or stakeholders have vague needs
- Process: gather initial requirements → build prototype → validate → formalize requirements → follow iterative model
- Prototype serves to clarify requirements rather than become the final product
- Examples: Instagram Reels first tested in India, Facebook reactions tested regionally
- Risk: multiple failed prototypes can be more wasteful than waterfall approach

### Agile Development (Extreme Programming)

- Even shorter cycles than iterative model
- Based on testable user stories that serve as requirements
- Features test-driven development: write tests before code
- Utilizes pair programming: senior and junior developers working together
- Typical sprint cycles of 2-4 weeks
- Focuses on present needs rather than future-proofing
- Potential drawbacks: constant sprints can be stressful, stand-ups sometimes misused for micromanagement

### Why Time Matters in Software Development

- The world changes: requirements evolve during long development cycles
- Computing environments change: hardware capabilities impact what's possible
- Business competition: faster companies can take market share
- Techniques become obsolete: companies that don't adapt lose users (Internet Explorer example)

---

## **What did we cover in the second hour?**

---

This lecture covers Extreme Programming (XP) methodology, focusing on continuous testing and its application in software development.

### Continuous Testing in Extreme Programming

Continuous testing ensures codebase stability but can be time-consuming for large projects. Test case prioritization helps by running only tests for potentially affected code areas. This approach maintains comprehensive testing while minimizing build time. Making smaller, incremental changes rather than comprehensive ones helps make testing quicker and bug identification easier.

### Key Characteristics of Extreme Programming

- Short development cycles compared to waterfall and iterative models
- Fine-grained, testable user stories
- Test-driven development (writing tests before implementation)
- Pair programming (one person on instrumentation, another on design)
- Continuous testing of micro-changes
- Frequent refactoring to maintain code quality

### When to Use Extreme Programming

- Projects with frequently changing requirements
- Mature software in maintenance phase
- When quick delivery is essential for business competition
- Startup environments where rapid feedback is crucial

### When Not to Use Extreme Programming

- Quality-critical software (military, NASA projects)
- Very large projects with large teams
- Projects without customer involvement in the feedback loop

### Comparison with Iterative Model

- XP conducts small tests for every change, enabling better regression tracking
- Iterative model tests only after implementation completion
- XP involves frequent refactoring, improving overall software quality
- XP requirements are more fine-grained and testable
- XP provides better customer confidence through ongoing involvement

### Semantic Versioning

Versioning follows the convention:

- First number: major changes
- Second number: minor changes
- Third number: patches or bug fixes

### Project Considerations

- [ ] Students to consider which development model to use for upcoming project
- [ ] Students to think about best practices for Git in team environments
- [ ] Students to plan how to handle bug reporting and code reviews
