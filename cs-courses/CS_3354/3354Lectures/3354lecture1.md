# **Date: June 3rd, 2025 -- Software Engineering**

---

## **What we covered in the first hour:**

This lecture covered the core principles of software engineering, exploring characteristics of software, quality attributes, stakeholder responsibilities, and best practices for development.

### Software Characteristics

Software has several distinctive characteristics that shape how it's developed:

- **Complexity**: Software evolves over time through added features and code modifications
- **Intangibility**: Cannot be physically touched, exists only as code
- **Evolution**: Software systems continuously branch and evolve to meet different needs

The Debian OS was presented as a prime example of software evolution. Starting in the 80s/90s, it branched into various forks including:

- Ubuntu - widely used general-purpose distribution
- Voodoo - designed to be beginner-friendly with accessible UI
- Kali - specialized for security professionals

### Quality Attributes in Software

Building high-quality software requires attention to:

- **Reliability**: Software must function correctly and consistently
- **Performance**: Processing time matters (10-second page loads create poor user experience)
- **Usability**: Applications should be intuitive (Google Maps vs. UTD maps comparison)
- **Maintainability**: 60% of software jobs involve maintaining existing code
- **Compatibility**: New features must integrate smoothly with existing architecture

### Software Engineering Principles

The lecture defined software engineering (from 1968) as "the establishment and use of sound engineering principles to obtain economically software that is reliable and works efficiently on real machines."

Key aspects of software engineering:

- Building quality software while managing time constraints
- Enhancing developer productivity through tools and practices
- Working in teams with different roles (programmers, testers, product managers)
- Employing version control systems like Git for collaboration

### Stakeholder Responsibilities

**Engineers should:**

- Focus on design quality, not just writing code
- Test code thoroughly (unit testing and integration testing)
- Follow established coding styles and documentation practices

**Managers should:**

- Manage resource allocation carefully
- Avoid adding developers late in projects
- Consider long-term maintenance implications when outsourcing

**Customers should:**

- Stay involved throughout development
- Communicate requirement changes early
- Understand that late-stage changes increase costs exponentially

### Notable Software Failures

The lecture highlighted several famous software failures:

- **PAC-MAN**: Level 256 displayed random symbols due to 8-bit integer limitation
- **USS Yorktown**: Naval ship stopped functioning for three hours when zero was entered in a data field
- **Y2K**: Created widespread concern but had less impact than anticipated

### When to Apply Software Engineering Principles

The level of formality in applying software engineering principles should match the project scope:

- One-time scripts require minimal process
- Libraries that interface with existing code need thorough testing
- Collaborative projects require documentation and version control
- Customer-facing applications need regular stakeholder involvement

## **What we covered in the second hour:**

---

This lecture covered the fundamentals of software development lifecycle models with a focus on the waterfall model, its applications, and limitations.

### Software Engineering Components

- Key components: tools, methods, and process models
- Quality focus is essential for developing high-quality software
- Tools help maintain code quality (e.g., linting tools that check code complexity)
- Process models outline the steps needed to build software artifacts

### The Waterfall Model Phases

- **Requirements Engineering**: Collecting specifications from stakeholders and documenting them in Software Requirement Specifications (SRS)
- **Design**: Creating a decoupled architecture where components have defined interfaces
- **Implementation**: Writing code for each module, typically developed in parallel
- **Integration**: Combining all implemented components and testing the whole system

### Applications of the Waterfall Model

- Best suited for projects with well-defined, stable requirements
- Appropriate for critical systems where bugs would be extremely costly
- Historically used in early software development when applications were less complex
- Example: NASA software projects with precise specifications

### Limitations and Challenges

- Difficult to implement changes once development has begun
- Iterations are expensive and time-consuming
- Less suitable for modern applications with evolving requirements
- Specifications can become overly complex and difficult for users to understand

### Contextual Comparisons

- NASA uses waterfall because bugs in deployed satellites are extremely costly
- Modern apps like Facebook use more Agile approaches where flexibility is prioritized
- The appropriate model depends on the cost of failures and requirement stability

### Next Steps

- [ ] Future classes will cover additional software development lifecycle processes
