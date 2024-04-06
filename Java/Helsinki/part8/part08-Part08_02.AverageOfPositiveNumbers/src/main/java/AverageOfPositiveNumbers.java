
import java.util.Scanner;

public class AverageOfPositiveNumbers {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int sum = 0;
        int index = 0;

        while (true) {
            int aveNum = scanner.nextInt();
            if (aveNum == 0) {
                break;
            } else if (aveNum < 0) {
                continue;
            } else {
                sum += aveNum;
                index += 1;
            }
        }
        if (index > 0) {
            double dousy = (double) sum / index;
            System.out.println(dousy);
        } else {
            System.out.println("nnot");
        }
    }
}
