import java.util.Scanner;

public class Login {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter username:");
        String inputUsername = scanner.nextLine();
        System.out.println("Enter password:");
        String inputUserPassword = scanner.nextLine();

        String[] user1 = {"alex", "sunshine"};
        String[] user2 = {"emma", "haskell"};

        if (inputUsername.equals(user1[0]) && inputUserPassword.equals(user1[1])) {
            System.out.println("You have successfully logged in!");
        } else if (inputUsername.equals(user2[0]) && inputUserPassword.equals(user2[1])) {
            System.out.println("You have successfully logged in!");
        } else {
            System.out.println("Incorrect username or password!");
        }
    }
}
