import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        ArrayList<TelevisionProgram> programs = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        // Read television programs from the user
        while (true) {
            System.out.print("Name: ");
            String name = scanner.nextLine();

            if (name.isEmpty()) {
                break;
            }

            System.out.print("Duration: ");
            int duration = Integer.parseInt(scanner.nextLine());

            programs.add(new TelevisionProgram(name, duration));
        }

        // Ask for the maximum duration
        System.out.print("Program's maximum duration? ");
        int maxDuration = Integer.parseInt(scanner.nextLine());

        // List programs with duration less than or equal to the specified maximum
        System.out.println("TV Programs within the maximum duration:");
        for (TelevisionProgram program : programs) {
            if (program.getDuration() <= maxDuration) {
                System.out.println(program);
            }
        }
    }
}
