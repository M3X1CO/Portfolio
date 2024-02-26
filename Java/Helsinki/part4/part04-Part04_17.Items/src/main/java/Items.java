
import java.util.ArrayList;
import java.util.Scanner;

public class Items {

    public static void main(String[] args) {
        // implement here your program that uses the class Item

        ArrayList<Item> items = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        // Read the names of persons from the user
        while (true) {
            System.out.println("Name: ");
            String name = scanner.nextLine();
            if (name.isEmpty()) {
                break;
            }


            // Add to the list a new person
            // whose name is the previous user input
            items.add(new Item(name));
        }

        // Print the number of the entered persons, and their individual information
        // System.out.println();
        // System.out.println("Persons in total: " + items.size());
        // System.out.println("Persons: ");

        for (Item person: items) {
            System.out.println(person);
        }
    }
}
