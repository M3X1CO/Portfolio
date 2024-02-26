
import java.util.Scanner;

public class PrintThrice {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Write your program here
        System.out.println("Give a word: ");
        String word = scanner.nextLine();
        int count = 3;
        String phrase = word.repeat(count);
        System.out.println(phrase);
    }
}
