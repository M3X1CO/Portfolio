
import java.util.Scanner;

public class SumOfASequence {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Last number? ");
        int numEnd = Integer.valueOf(scanner.nextLine());
        int numSum = 0;
        int index = 0;
        while (index < numEnd) {
            index++;
            numSum += index;
        }
        System.out.println(numSum);
    }
}
