
import java.util.Scanner;

public class AVClub {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String beans = scanner.nextLine();
            if (beans.equals("")) {
                return;
            }
            String[] cheese = beans.split(" ");
            for (int i = 0; i < cheese.length; i++) {
                String theory = cheese[i];
                if (theory.contains("av")) {
                    System.out.println(theory);
                }
            }
        }
    }
}
