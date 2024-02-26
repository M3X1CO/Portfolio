
import java.util.Scanner;

public class SimpleCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Write your program here
        System.out.println("Give the first number:");
        int one = Integer.valueOf(scanner.nextLine());
        System.out.println("Give the second number:");
        int two = Integer.valueOf(scanner.nextLine());
        int add = one + two;
        int sub = one - two;
        int mult = one * two;
        double div = (double) one / two;
        System.out.println(one + " + " + two + " = " + add);
        System.out.println(one + " - " + two + " = " + sub);
        System.out.println(one + " * " + two + " = " + mult);
        System.out.println(one + " / " + two + " = " + div);
        
    }
}
