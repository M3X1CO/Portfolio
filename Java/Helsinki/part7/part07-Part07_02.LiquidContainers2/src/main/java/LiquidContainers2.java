
import java.util.Scanner;

public class LiquidContainers2 {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Container containerOne = new Container();
        Container containerTwo = new Container();
        
        UserInterface userInterface = new UserInterface(containerOne, containerTwo, scan);
        userInterface.start();
    }
}