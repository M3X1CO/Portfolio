import java.util.Scanner;

public class MainProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Statistics statistics = new Statistics();
        Statistics evenNumber = new Statistics();
        Statistics oddNumber = new Statistics();

        System.out.println("Enter numbers: ");
        while (true) {
            int userInput = Integer.valueOf(scanner.nextLine());
            if (userInput == -1) {
                break;
            } else if (userInput % 2 ==0) {
                statistics.addNumber(userInput);
                evenNumber.addNumber(userInput);
            } else {
                statistics.addNumber(userInput);
                oddNumber.addNumber(userInput);
            }
        }
        // System.out.println("Count: " + statistics.getCount());
        System.out.println("Sum: " + statistics.sum());
        // System.out.println("Average: " + statistics.average());
        System.out.println("Sum of even numbers: " + evenNumber.sum());
        System.out.println("Sum of odd numbers: " + oddNumber.sum());
    }
}