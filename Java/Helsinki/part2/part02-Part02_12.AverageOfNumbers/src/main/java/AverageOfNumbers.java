
import java.util.Scanner;

public class AverageOfNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numNums = 0;
        double numSums = 0;
        double numAvg = 0;
        while (true) {
            System.out.println("Give a number:");
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            } else {
                numNums += 1;
                numSums += number;
            }
        }
        if (numSums != 0) {
            numAvg = (double) numSums / numNums;
        }
        System.out.println("Average of the numbers: " + numAvg);
    }
}
