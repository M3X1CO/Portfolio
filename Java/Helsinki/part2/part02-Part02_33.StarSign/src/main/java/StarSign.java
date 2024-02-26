
public class StarSign {

    public static void main(String[] args) {

        
        //The tests are not checking the main, so you can modify it freely.
        //NB: If the tests don't seem to pass, you should try the methods here
        //in the main to make sure they print the correct shapes!
        
        printStars(3);
        System.out.println("\n---");  // printing --- between the shapes
        printSquare(4);
        System.out.println("\n---");
        printRectangle(5, 6);
        System.out.println("\n---");
        printTriangle(3);
        System.out.println("\n---");
    }

    public static void printStars(int number) {
        // first part of the exercise
        int index = 0;
        while (index < number) {
            System.out.print("*");
            index++;
        }
        System.out.println("");
    }

    public static void printSquare(int size) {
        // second part of the exercise
        int index = 0;
        while (index < size) {
            printStars(size);
            index++;
        }
    }

    public static void printRectangle(int width, int height) {
        // third part of the exercise
        int index = 0;
        while (index < height) {
            printStars(width);
            index++;
        }
    }

    public static void printTriangle(int size) {
        // fourth part of the exercise
        int start = 0;
        int index = size;
        while (index > 0) {
            start++;
            index--;
            printStars(start);
        }
    }
}
