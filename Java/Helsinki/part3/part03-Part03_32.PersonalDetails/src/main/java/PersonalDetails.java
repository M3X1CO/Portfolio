
import java.util.ArrayList;
import java.util.Scanner;

public class PersonalDetails {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double sumYear = 0;
        int theory = 0;
        int numLong = 0;
        String name = "";
        while (true) {
            String beans = scanner.nextLine();
            if (beans.equals("")) {
                break;
            }
            String[] cheese = beans.split(",");
            theory ++;
            sumYear += Double.valueOf(cheese[1]);
            
            String word = cheese[0];
            int length = word.length();
            if (length > numLong) {
                numLong = length;
                name = word;
            }
            
        }
        System.out.println("Longest name: " + name);
        System.out.println("Average of the birth years: " + (double)(sumYear / theory));
    }
}