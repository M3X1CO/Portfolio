

public class FromOneToParameter {

    public static void main(String[] args) {
        printUntilNumber(5);
    }
    
    public static void printUntilNumber(int number) {
        int index = 0;
        while (index < number) {
            index++;
            System.out.println(index);
        }
    }

}
