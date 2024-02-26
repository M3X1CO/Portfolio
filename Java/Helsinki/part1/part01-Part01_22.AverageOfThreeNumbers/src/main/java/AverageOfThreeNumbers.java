
import java.util.Scanner;

public class AverageOfThreeNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Write your program here
        System.out.println("Give the first number:");
        int one = Integer.valueOf(scanner.nextLine());
        System.out.println("Give the second number:");
        int two = Integer.valueOf(scanner.nextLine());
        System.out.println("Give the third number:");
        int tree = Integer.valueOf(scanner.nextLine());
        double avg = (double) (one + two + tree) / 3;
        System.out.println("The average is " + avg);
    }
}
