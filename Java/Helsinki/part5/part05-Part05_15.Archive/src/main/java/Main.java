
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Objects> collection = new ArrayList<>();
        
        while (true) {
            System.out.println("Identifier? (empty will stop)");
            String identifier = scanner.nextLine();
            
            if (identifier.isEmpty()) {
                break;
            }

            System.out.println("Name? (empty will stop)");
            String name = scanner.nextLine();
            
            if (name.isEmpty()) {
                break;
            }

            Objects object = new Objects(identifier, name);
            
            boolean identifierExists = false;
            for (Objects obj : collection) {
                if (obj.getIdentifier().equals(identifier)) {
                    identifierExists = true;
                    break;
                }
            }
            if (identifierExists) {
                continue;
            }
            
            collection.add(object);

            
        }
        System.out.println("==Items==");
        for (Object item : collection) {
                System.out.println(item);
        } 
    }
}
