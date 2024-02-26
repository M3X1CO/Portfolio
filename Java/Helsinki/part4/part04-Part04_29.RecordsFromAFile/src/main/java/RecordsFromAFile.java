
import java.nio.file.Paths;
import java.util.Scanner;

public class RecordsFromAFile {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Name of the file: ");
        String file = scanner.nextLine();
        
        try (Scanner reader = new Scanner(Paths.get(file))) {
            while (reader.hasNextLine()) {
                String row = reader.nextLine();
                if (row.equals("")) {
                    break;
                }

                String[] parts = row.split(",");
                String name = parts[0];
                int age = Integer.valueOf(parts[1]);

                System.out.println(name + ", age: " + age + " years");
            }
        } catch (Exception e) {
            System.out.println("Danger Will Robinson");
        }
    }
}
