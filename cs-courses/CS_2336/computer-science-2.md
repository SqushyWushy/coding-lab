CS 2336 (COSC 2336) Computer Science II (3 semester credit hours) Further applications of programming techniques, introducing the fundamental concepts of data structures and algorithms. Topics include recursion, fundamental data structures (including stacks, queues, linked lists, hash tables, trees, and graphs), and algorithmic analysis. Includes comprehensive programming projects. Programming language of choice is Java.
Perfect — CS 2336: Computer Science II is where you really start learning to think like a computer scientist.

This class takes all the Java/OOP skills from COSC 1437 and turns up the difficulty by teaching you data structures, recursion, and algorithmic thinking. This is where you go from just writing code to writing efficient, elegant code.

⸻

1. Recursion
   • A function that calls itself

int factorial(int n) {
if (n <= 1) return 1;
return n \* factorial(n - 1);
}

Learn when recursion is helpful (like trees, backtracking) and when it’s dangerous (stack overflow).

⸻

2. Stacks
   • LIFO (Last-In, First-Out)
   • Used in undo operations, expression parsing

Stack<Integer> s = new Stack<>();
s.push(1); s.pop();

⸻

3. Queues
   • FIFO (First-In, First-Out)
   • Used in scheduling, BFS, task processing

Queue<Integer> q = new LinkedList<>();
q.add(1); q.remove();

⸻

4. Linked Lists
   • Nodes pointing to the next (and maybe previous) node
   • Types: Singly, Doubly, Circular

class Node {
int data;
Node next;
}

⸻

5. Hash Tables (HashMaps)
   • Key-value pairs for fast lookup (like a dictionary)

HashMap<String, Integer> map = new HashMap<>();
map.put("apples", 5); map.get("apples");

You learned about hash functions, collisions, and how to handle them (like chaining).

⸻

6. Trees (esp. Binary Trees, BSTs)
   • Hierarchical structures
   • Depth-first & Breadth-first traversal

class TreeNode {
int val;
TreeNode left, right;
}

Understand in-order, pre-order, post-order traversal and binary search tree rules.

⸻

7. Graphs
   • Nodes + edges (directed/undirected, weighted/unweighted)
   • Represented using adjacency lists or matrices

You may have learned DFS, BFS, and maybe even Dijkstra’s Algorithm.

⸻

8. Big-O Analysis (Algorithmic Efficiency)
   • How fast is your code, really?
   • You learned how to estimate:
   • Time complexity (O(n), O(log n), O(n^2), etc.)
   • Space complexity

This is crucial for interviews and real-world coding.

⸻

9. Sorting Algorithms
   • Bubble, Selection, Insertion, Merge, Quick

Know how they work and their Big-O:

Bubble Sort: O(n^2)
Merge Sort: O(n log n)

⸻

10. Real Projects

You probably built:
• A custom linked list class
• A simple text editor with undo/redo
• A mini database or address book using HashMap
• A binary search tree visualizer or pathfinder
