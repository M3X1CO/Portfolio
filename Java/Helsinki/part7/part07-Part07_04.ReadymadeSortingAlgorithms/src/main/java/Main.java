
import java.util.*;



public class Main {

    public static void main(String[] args) {
        // insert test code here
        int[] array = {8, 3, 7, 9, 1, 2, 4};
        
        String[] names = {"allen", "charlie", "dick", "zed's_dead", "ingra", "watson", "lily"};
        
        ArrayList<Integer> integers = new ArrayList<>();
        integers.add(5);
        integers.add(123);
        integers.add(23);
        integers.add(54);
        integers.add(67);
        integers.add(8);
        
        ArrayList<String> words = new ArrayList<>();
        words.add("Apple");
        words.add("fapple");
        words.add("topple");
        words.add("dapple");
        words.add("wrapple");
        words.add("snapple");
        words.add("cApple");
        words.add("Attapple");
        words.add("sApple");
        
        sort(array);
        sort(names);
        sortIntegers(integers);
        sortStrings(words);
        
    }
    
    public static void sort(int[] array) {
        System.out.println(Arrays.toString(array));
        Arrays.sort(array);
        System.out.println(Arrays.toString(array));
    }
    
    public static void sort(String[] names) {
        System.out.println(Arrays.toString(names));
        Arrays.sort(names);
        System.out.println(Arrays.toString(names));
    }
    
    public static void sortIntegers(ArrayList<Integer> integers) {
        System.out.println(integers);
        Collections.sort(integers);
        System.out.println(integers);
    }
    
    public static void sortStrings(ArrayList<String> words) {
        System.out.println(words);
        Collections.sort(words);
        System.out.println(words);
    }

}
