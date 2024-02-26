
import java.util.Scanner;

public class AbsoluteValue {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nums = Integer.valueOf(scanner.nextLine());
        
        if (nums < 0){
            nums = nums * -1;
            System.out.println(nums);
        } else {
            System.out.println(nums);
        }
    }
}
