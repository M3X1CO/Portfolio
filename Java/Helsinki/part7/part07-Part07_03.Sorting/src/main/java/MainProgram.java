
public class MainProgram {

    public static void main(String[] args) {
        // write your test code here
        int[] numbers = {8, 3, 7, 9, 1, 2, 4};
        MainProgram.sort(numbers);
    }
    
    public static int smallest(int[] array) {
        // write your code here
        int lowestNumber = array[0];
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] < lowestNumber) {
                lowestNumber = array[i];
            }
        }
        return lowestNumber;
    }
    
    public static int indexOfSmallest(int[] array) {
        // write your code here
        int lowestNumber = array[0];
        int lowestNumberIndex = 0;
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] < lowestNumber) {
                lowestNumber = array[i];
                lowestNumberIndex = i;
            }
        }
        return lowestNumberIndex;
    }
    
    public static int indexOfSmallestFrom(int[] table, int startIndex) {
        // write your code here
        int lowestNumber = table[startIndex];
        int lowestNumberIndex = startIndex;
        
        for (int i = startIndex; i < (table.length); i++) {
            if (table[i] < lowestNumber) {
                lowestNumber = table[i];
                lowestNumberIndex = i;
            }
        }
        return lowestNumberIndex;
    }
    
    public static void swap(int[] array, int index1, int index2) {
        // write your code here
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
        
    }
    
    public static void sort(int[] array) {

        for (int startIndex = 0; startIndex < array.length; startIndex++) {
            int smallestIndex = indexOfSmallestFrom(array, startIndex);
            swap(array, startIndex, smallestIndex);
        }
    }
}
