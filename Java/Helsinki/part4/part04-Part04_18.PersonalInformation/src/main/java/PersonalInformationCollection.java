import java.util.ArrayList;
import java.util.Scanner;

public class PersonalInformationCollection {

    public static void main(String[] args) {
        // implement here your program that uses the PersonalInformation class

        ArrayList<PersonalInformation> infoCollection = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        // Read the names of persons from the user
        while (true) {
            System.out.println("First name: ");
            String firstName = scanner.nextLine();
            if (firstName.isEmpty()) {
                break;
            }
            
            System.out.println("Last name: ");
            String lastName = scanner.nextLine();
            if (lastName.isEmpty()) {
                break;
            }
            
            System.out.println("Identification number: ");
            String identificationNumber = scanner.nextLine();
            if (identificationNumber.isEmpty()) {
                break;
            }

            // Add to the list a new person
            // whose name is the previous user input
            infoCollection.add(new PersonalInformation(firstName, lastName, identificationNumber));
        }

        for (PersonalInformation person : infoCollection) {
            System.out.println(person.getFirstName() + " " + person.getLastName());
            // System.out.println("Identification number: " + person.getIdentificationNumber());
            // System.out.println();  // Add an empty line for better readability
        }
    }
}
