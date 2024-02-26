
import java.util.Scanner;

public class SumOfASequenceTheSequel {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int numSum = 0;
        System.out.println("First number? ");
        int numStart = Integer.valueOf(scanner.nextLine());
        System.out.println("Last number? ");
        int numEnd = Integer.valueOf(scanner.nextLine());
        while (numStart <= numEnd) {
            numSum += numStart;
            numStart++;
        }
        System.out.println(numSum);
    }
}
