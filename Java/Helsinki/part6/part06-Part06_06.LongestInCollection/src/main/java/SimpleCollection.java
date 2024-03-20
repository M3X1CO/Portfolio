
import java.util.ArrayList;

public class SimpleCollection {

    private String name;
    private ArrayList<String> elements;

    public SimpleCollection(String name) {
        this.name = name;
        this.elements = new ArrayList<>();
    }

    public void add(String element) {
        this.elements.add(element);
    }

    public ArrayList<String> getElements() {
        return this.elements;
    }
    
    public String longest() {
        int indexCount = 0;
        String longest = "";
        if (this.elements.isEmpty()) {
            return null;
        }
        
        for (String same: elements) {
            if (same.length() > indexCount) {
                indexCount = same.length();
                longest = same;
            }
        }
        return longest;
    }

}
