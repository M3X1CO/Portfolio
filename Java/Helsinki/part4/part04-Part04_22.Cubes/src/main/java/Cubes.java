import java.util.Scanner;

public class Cubes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int intResult = 0;

        while (true) {
            String userInput = scanner.nextLine();

            if (userInput.equals("end")) {
                break;
            }

            int intValue = Integer.parseInt(userInput);

            intResult += intValue * intValue * intValue;
            System.out.println(intResult);
            intResult = 0;
        }
    }
}
