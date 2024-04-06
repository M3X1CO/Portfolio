
import java.util.ArrayList;

public class Recipe {
    
    private String name;
    private int time;
    private ArrayList<String> ingredients;
    
    public Recipe(String name, int time, ArrayList<String> ingredients) {
        this.name = name;
        this.time = time;
        this.ingredients = ingredients;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setTime(int time) {
        this.time = time;
    }
    
    public void ingredients(ArrayList<String> ingredients) {
        this.ingredients = ingredients;
    }
    
    public String getName() {
        return this.name;
    }
    
    public int getTime() {
        return this.time;
    }
    
    public ArrayList<String> getIngredients() {
        return this.ingredients;
    }
    
    @Override
    public String toString() {
        return this.name + ", " + "cooking time: " + this.time;
    }
}
