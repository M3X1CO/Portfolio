
import java.util.ArrayList;

public class Menu {

    private ArrayList<String> meals;

    public Menu() {
        this.meals = new ArrayList<>();
    }

    // implement the required methods here
    
    // Add a meal to the array
    public void addMeal(String meal){
        if (!this.meals.contains(meal)) {
            this.meals.add(meal);
        }
    }
    
    // Prints out the current stored meals in the array
    public void printMeals() {
        for (String meal: this.meals) {
            System.out.println(meal);
        }
    }
    
    
    // Removes all of the meals from the array
    public void clearMenu() {
        this.meals.clear();
    }
}
