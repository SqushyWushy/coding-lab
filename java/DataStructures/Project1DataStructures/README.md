# PROJECT 1 - LINKED LIST

**NAME:** Jr Hector Gonzalez

**DATE:** 9/30/2025

**IDE:** None - Used Zed text editor and compiled/ran via command line

## What It Is

This is a linked list program for managing products.
The assignment wanted us to make an interface, a product class, a generic
linked list, and a menu program.

## Files

- `IDedObject.java` - interface
- `Product.java` - product class with ID, name, supplier
- `GenericLinkedList.java` - the linked list
- `ProductManager.java` - main program with menu
- `README.md` - this file

## How to Compile

```bash
cd java/DataStructures/Project1DataStructures
javac *.java
```

## How to Run

```bash
java ProductManager
```

## How It Works

You get a menu with 7 options:

1. **Make Empty** - clears the list
2. **Find ID** - search for a product
3. **Insert At Front** - add a product
4. **Delete From Front** - remove first product
5. **Delete ID** - remove specific product
6. **Print All Records** - show everything
7. **Done** - quit

## Sample Output

```
Operations on List
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 3
Enter Product ID: 1111
Enter Product Name: ABC Book
Enter Supplier Name: Scholastic
Product Added

Operations on List
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 2
ID No: 1111
1111
ABC Book
Scholastic

Operations on List
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 4
1111
ABC Book
Scholastic
First item deleted

Operations on List
1. Make Empty
2. Find ID
3. Insert At Front
4. Delete From Front
5. Delete ID
6. Print All Records
7. Done
Your choice: 7
Done.
```

## What Works

Everything the assignment asked for works:

- Interface with getID and printID
- Product class with private variables
- Generic linked list
- All the menu options
- No duplicate IDs allowed
- Handles empty list

## What Doesn't Work

Everything works fine I hope

## Notes

I kept it simple. Used if-else instead of switch because it's easier at least I think so.
No fancy error handling stuff as I'm not the best and no time to re-learn it all.
Kept the comments pretty simple but you can tell what everything does.

The hardest part was the delete function where you have to track the node
before the one you want to delete.
