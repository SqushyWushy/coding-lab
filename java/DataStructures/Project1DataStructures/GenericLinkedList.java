// generic linked list class
public class GenericLinkedList<AnyType extends IDedObject> {

    // node class
    private class Node {
        AnyType data;
        Node next;

        public Node(AnyType data) {
            this.data = data;
            this.next = null;
        }
    }

    private Node head;

    // constructor
    public GenericLinkedList() {
        head = null;
    }

    // makes list empty
    public void makeEmpty() {
        head = null;
    }

    // finds object by ID
    public AnyType findID(int ID) {
        if (head == null) {
            return null;
        }

        Node current = head;
        while (current != null) {
            if (current.data.getID() == ID) {
                return current.data;
            }
            current = current.next;
        }
        return null;
    }

    // insert at front
    public boolean insertAtFront(AnyType x) {
        // check if ID exists
        if (findID(x.getID()) != null) {
            return false;
        }

        Node newNode = new Node(x);
        newNode.next = head;
        head = newNode;
        return true;
    }

    // delete from front
    public AnyType deleteFromFront() {
        if (head == null) {
            return null;
        }

        AnyType data = head.data;
        head = head.next;
        return data;
    }

    // delete by ID
    public AnyType delete(int ID) {
        if (head == null) {
            return null;
        }

        // check if its the first one
        if (head.data.getID() == ID) {
            AnyType data = head.data;
            head = head.next;
            return data;
        }

        // look through the rest
        Node current = head;
        while (current.next != null) {
            if (current.next.data.getID() == ID) {
                AnyType data = current.next.data;
                current.next = current.next.next;
                return data;
            }
            current = current.next;
        }
        return null;
    }

    // print everything
    public void printAllRecords() {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }

        Node current = head;
        while (current != null) {
            current.data.printID();
            if (current.next != null) {
                System.out.println();
            }
            current = current.next;
        }
    }
}
