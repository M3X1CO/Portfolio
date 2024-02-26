
import java.util.Scanner;

public class AgeOfTheOldest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOld = 0;
        while (true) {
            String beans = scanner.nextLine();
            if (beans.equals("")) {
                break;
            }
            String[] cheese = beans.split(",");
            for (int i = 0; i < cheese.length; i++) {
                if (Integer.valueOf(cheese[1]) > numOld) {
                    numOld = Integer.valueOf(cheese[1]);
                }
            }
        }
        System.out.println("Age of the oldest: " + numOld);
    }
}
