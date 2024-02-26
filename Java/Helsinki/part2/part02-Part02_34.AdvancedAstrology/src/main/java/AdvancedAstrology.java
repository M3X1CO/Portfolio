
public class AdvancedAstrology {

    public static void printStars(int number) {
        // part 1 of the exercise
        int index = 0;
        while (index < number) {
            System.out.print("*");
            index++;
        }
        System.out.println("");
    }

    public static void printSpaces(int number) {
        // part 1 of the exercise
        int index = 0;
        while (index < number) {
            System.out.print(" ");
            index++;
        }
    }

    public static void printTriangle(int size) {
        // part 2 of the exercise
        int start = 0;
        int space = size;
        while (space > 0) {
            start++;
            space--;
            printSpaces(space);
            printStars(start);
        }
    }

    public static void christmasTree(int height) {
        // part 3 of the exercise
        int start = 0;
        int index = height;

        while (index > 0) {
            index--;
            start++;
            printSpaces(index);
            printStars(start+start-1);
        }
        int treeBase = 0;
        while (treeBase < 2) {
            printSpaces(height-2);
            printStars(3);
            treeBase++;
        }
    }

    public static void main(String[] args) {
        // The tests are not checking the main, so you can modify it freely.

        printTriangle(5);
        System.out.println("---");
        christmasTree(4);
        System.out.println("---");
        christmasTree(10);
    }
}
