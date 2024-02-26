
import java.util.Scanner;

public class RepeatingBreakingAndRemembering {

    public static void main(String[] args) {
        
        // This exercise is worth five exercise points, and it is 
        // gradually extended part by part.
        
        // If you want, you can send this exercise to the server
        // when it's just partially done. In that case the server will complain about 
        // the parts you haven't done, but you'll get points for the finished parts.
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Give numbers:");
        
        int count = 0;
        int numSums = 0;
        double numAvg = 0;
        int numEven = 0;
        int numOdd = 0;
        while (true) {
            int numbers = Integer.valueOf(scanner.nextLine());
            if (numbers == -1) {
                break;
            } else {
                numSums += numbers;
                count++;
                if (numbers % 2 == 0) {
                    numEven++;
                } else {
                    numOdd++;
                }
            }
        }
        System.out.println("Thx Bye!");
        System.out.println("Sum:" + numSums);
        System.out.println("Numbers: " + count);
        System.out.println("Average: " + (double) numSums/count);
        System.out.println("Even: " + numEven);
        System.out.println("Odd: " + numOdd);
    }
}
