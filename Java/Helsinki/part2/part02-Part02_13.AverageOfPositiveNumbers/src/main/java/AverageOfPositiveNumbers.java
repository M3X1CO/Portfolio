
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numNums = 0;
        double numSums = 0;
        double avgNums = 0;
        while (true) {
            int number = Integer.valueOf(scanner.nextLine());
            if (number == 0) {
                break;
            } else if (number > 0) {
                numNums += 1;
                numSums += number;
            }
        }
        if (numNums > 0) {
            avgNums = numSums / numNums;
            System.out.println(avgNums);
        } else {
            System.out.println("Cannot calculate the average");
        }
        
    }
}
