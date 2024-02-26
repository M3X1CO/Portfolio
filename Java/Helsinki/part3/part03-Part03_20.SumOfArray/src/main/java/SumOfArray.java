
import java.util.Scanner;

public class SumOfArray {

    public static void main(String[] args) {
        // You can try the method here
        int[] array = {5, 1, 3, 4, 2};
        sumOfNumbersInArray(array);

        // Swapping example (as in your original code)
        Scanner scanner = new Scanner(System.in);
        System.out.println("Give two indices to swap:");
        int num1 = Integer.valueOf(scanner.nextLine());
        int num2 = Integer.valueOf(scanner.nextLine());
        int helper = array[num1];
        array[num1] = array[num2];
        array[num2] = helper;

        // Print the array after swapping
        sumOfNumbersInArray(array);
    }

    public static int sumOfNumbersInArray(int[] array) {
        int sumNum = 0;
        for (int number : array) {
            System.out.println(number);
            sumNum += number;
        }
        return sumNum;
    }
}
