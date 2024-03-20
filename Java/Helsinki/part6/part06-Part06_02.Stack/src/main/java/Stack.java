/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */
import java.util.ArrayList;



public class Stack {
    private ArrayList<String> items;
    
    // Initializing instance variables
    public Stack() {
        this.items = new ArrayList<>();
    }
    
    // Returns a boolean whether the list is empty
    public boolean isEmpty() {
        return this.items.isEmpty();
    }
    
    // Add a string value to the list
    public void add(String value) {
        this.items.add(value);
    }
    
    // Return a list of strings contained in the stack
    public ArrayList<String> values() {
        ArrayList<String> result = new ArrayList<>();
        for (String item: items) {
            result.add(item);
        }
        return result;
    }
    
    // Look at the last item in the stack
    public String take() {
    if (!isEmpty()) {
        int lastValue = items.size() - 1;
        String value = items.get(lastValue);
        items.remove(lastValue);
        return value;
    }
    return null;
}

}
