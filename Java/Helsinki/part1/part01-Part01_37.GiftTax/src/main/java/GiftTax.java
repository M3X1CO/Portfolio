
import java.util.Scanner;

public class GiftTax {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        //todo
        System.out.println("Value of the gift?");
        int tax = Integer.valueOf(scan.nextLine());
        double tax1 = (100 + (tax - 5000) * 0.08);
        double tax2 = (1700 + (tax - 25000) * 0.10);
        double tax3 = (4700 + (tax - 55000) * 0.12);
        double tax4 = (22100 + (tax - 200000) * 0.15);
        double tax5 = (142100 + (tax - 1000000) * 0.17);
        if (tax < 5000) {
            System.out.println("No tax!");
        } else if (tax < 25001) {
            System.out.println("Tax: " + tax1);
        } else if (tax < 55001) {
            System.out.println("Tax: " + tax2);
        } else if (tax < 200001) {
            System.out.println("Tax: " + tax3);
        } else if (tax < 1000001) {
            System.out.println("Tax: " + tax4);
        } else if (tax > 1000000) {
            System.out.println("Tax: " + tax5);
        }
    }
}
