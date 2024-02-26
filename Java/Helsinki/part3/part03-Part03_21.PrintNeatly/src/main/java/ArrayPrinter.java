
public class ArrayPrinter {

    public static void main(String[] args) {
        // You can test your method here
        int[] array = {5, 1, 3, 4, 2};
        printNeatly(array);
    }

    public static void printNeatly(int[] array) {
        // Write some code in here
        int count = array.length-1;
        String beans = ", ";
        for (int i = 0; i < array.length; i++) {
            int number = array[i];
            System.out.print(number);
            if (count > 0) {
                System.out.print(beans);
                count--;
            }
        }
    }
}
