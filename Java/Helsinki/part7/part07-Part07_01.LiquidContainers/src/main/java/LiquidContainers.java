
import java.util.Scanner;

public class LiquidContainers {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int containerOne = 0;
        int containerTwo = 0;
        int maxVolume = 100;

        while (true) {
            
            System.out.println("First: " + containerOne + "/" + maxVolume);
            System.out.println("Second: " + containerTwo + "/" + maxVolume);
            
            String input = scan.nextLine();
            if (input.equals("quit")) {
                break;
            }
            String[] parts = input.split(" ");

            String command = parts[0];
            int amount = Integer.valueOf(parts[1]);
            
            if (amount >= 0 && command.equals("add")) {
                if (containerOne + amount >= maxVolume) {
                    containerOne = maxVolume;
                } else {
                    containerOne += amount;
                }
            } else if (amount >= 0 && command.equals("move")) {
                if (amount > containerOne) {
                    containerTwo += containerOne;
                    containerOne = 0;
                    if (containerTwo > maxVolume) {
                        containerTwo = maxVolume;
                    }
                } else {
                    containerTwo += amount;
                    containerOne -= amount;
                    if (containerTwo > maxVolume) {
                        containerTwo = maxVolume;
                    }
                }
            } else if (amount >= 0 && command.equals("remove")) {
                containerTwo -= amount;
                if (containerTwo < 0) {
                    containerTwo = 0;
                }
            }

        }
    }

}
