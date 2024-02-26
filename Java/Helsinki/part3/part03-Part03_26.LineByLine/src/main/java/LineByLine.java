
import java.util.Scanner;

public class LineByLine {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);     
        
        while (true) {
            String beans = scanner.nextLine();
            if (beans.equals("")) {
                return;
            }
            String[] cheese = beans.split(" ");
            for (int i = 0; i < cheese.length; i++) {
                System.out.println(cheese[i]);
            }
        }
    }
}
