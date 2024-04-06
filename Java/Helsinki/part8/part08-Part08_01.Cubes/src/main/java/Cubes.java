
import java.util.Scanner;

public class Cubes {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        while (true) {
            String cube = scanner.nextLine();
            
            if (cube.equals("end")) {
                break;
            } else {
                int cubed = Integer.valueOf(cube) * Integer.valueOf(cube) * Integer.valueOf(cube);
                System.out.println(cubed);
            }
        }
    }
}
