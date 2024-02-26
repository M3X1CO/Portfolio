
import java.util.Scanner;

public class FirstWords {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String beans = scanner.nextLine();
            String[] cheese = beans.split(" ");
            if (beans.equals("")) {
                return;
            }
            System.out.println(cheese[0]);
        }
    }
}
