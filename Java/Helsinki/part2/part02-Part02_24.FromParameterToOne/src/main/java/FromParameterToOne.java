

public class FromParameterToOne {

    public static void main(String[] args) {
        printFromNumberToOne(5);
    }
    public static void printFromNumberToOne(int number) {
        for (int index = number; index > 0; index--) {
            System.out.println(index);
        }
    }
}
