
import java.util.Scanner;

public class NumberOfStrings {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int index = 0;
        
        while (true) {
            String userInput = scanner.nextLine();
            if (userInput.equals("end")) {
                break;
            }
            index += 1;
        }
        System.out.println(index);
    }
}
