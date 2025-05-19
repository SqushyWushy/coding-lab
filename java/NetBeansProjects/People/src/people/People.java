package people;

/**
 * Jr Hector Gonzalez
 * 04/19/24
 * This program is to design a class named Person and a class named Employee
 * which extends the Person class.
 */
public class People {
    public static void main(String[] args) {
        Person people[] = new Person[4];
        people[0] = new Person("Hector", "555-555-5555", "hector@gmail.com");
        people[1] = new Person("Daniel", "777-777-7777", "daniel@gmail.com");
        people[2] = new Employee("Mike", "999-999-9999", "mike@work.com", "1001");
        people[3] = new Employee("Mac", "111-111-1111", "mac@work.com", "1002"); 
        
        for (int i = 0; i < people.length;i++) {
            System.out.println(people[i]);
            System.out.println();
        }
    }
    
}
