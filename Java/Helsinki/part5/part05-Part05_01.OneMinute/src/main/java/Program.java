
import java.util.Scanner;

public class Program {

    public static void main(String[] args) {
        // You can test your program here
        Scanner scan = new Scanner(System.in);
        
        Timer timer = new Timer();

        while (true) {
            System.out.println(timer);
            timer.advance();

            try {
                Thread.sleep(10);
            } catch (Exception e) {

            }
        }
    }
}
