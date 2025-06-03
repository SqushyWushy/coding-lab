This course focuses on the object-oriented programming paradigm, emphasizing the definition and use of classes along with fundamentals of object-oriented design. The course includes basic analysis of algorithms, searching and sorting techniques, and an introduction to software engineering processes. Students will apply techniques for testing and debugging software.
Awesome — COSC 1437: Programming Fundamentals II is the “level up” to COSC 1436. Since you used Java, this class was all about object-oriented programming (OOP) — which is basically how to organize and structure bigger programs like a pro.

⸻

1. Classes & Objects
   • Class: a blueprint (like a recipe)
   • Object: a real thing built from that blueprint

public class Dog {
String name;
void bark() {
System.out.println(name + " says woof!");
}
}

Dog d = new Dog();
d.name = "Buddy";
d.bark();

⸻

2. Encapsulation
   • Hide the details inside the class using private variables and getters/setters.

public class BankAccount {
private double balance;

    public void deposit(double amount) {
        balance += amount;
    }

    public double getBalance() {
        return balance;
    }

}

⸻

3. Constructors
   • Special methods that run when you create an object.

public class Student {
String name;

    public Student(String n) {
        name = n;
    }

}

⸻

4. Inheritance
   • One class “inherits” from another.

public class Animal {
void speak() {
System.out.println("Animal speaks");
}
}

public class Dog extends Animal {
void speak() {
System.out.println("Dog barks");
}
}

⸻

5. Polymorphism
   • Same method name, different behavior based on the object.

Animal a = new Dog();
a.speak(); // Outputs "Dog barks" — not "Animal speaks"

⸻

6. Arrays & ArrayLists

int[] nums = {1, 2, 3};
ArrayList<String> names = new ArrayList<>();
names.add("Alice");

⸻

7. Searching & Sorting Algorithms
   • Linear Search
   • Binary Search
   • Bubble Sort, Selection Sort, etc.

You probably learned how to trace their steps and analyze speed using Big-O notation (e.g., O(n), O(log n)).

⸻

8. Interfaces & Abstract Classes
   • Create reusable templates for multiple classes.

interface Animal {
void makeSound();
}

⸻

9. Intro to Software Engineering Concepts
   • How to write testable code
   • Importance of modular design
   • Possibly touched on UML diagrams or design patterns

⸻

10. Unit Testing & Debugging
    • Writing test cases
    • Using print statements or debuggers to find bugs

⸻
