
import java.util.Scanner;

public class NameOfTheOldest {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numOld = 0;
        String numName = "";
        while (true) {
            String beans = scanner.nextLine();
            if (beans.equals("")) {
                break;
            }
            String[] cheese = beans.split(",");
            for (int i = 0; i < cheese.length; i++) {
                if (Integer.valueOf(cheese[1]) > numOld) {
                    numOld = Integer.valueOf(cheese[1]);
                    numName = cheese[0];
                }
            }
        }
        System.out.println("Name of the oldest: " + numName);
    }
}