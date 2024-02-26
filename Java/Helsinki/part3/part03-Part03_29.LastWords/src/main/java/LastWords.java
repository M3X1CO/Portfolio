
import java.util.Scanner;

public class LastWords {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String beans = scanner.nextLine();
            String[] cheese = beans.split(" ");
            if (beans.equals("")) {
                return;
            }
            int count = cheese.length;
            System.out.println(cheese[count-1]);
        }
    }
}