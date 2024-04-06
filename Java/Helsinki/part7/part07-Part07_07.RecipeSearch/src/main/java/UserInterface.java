import java.nio.file.Paths;
import java.util.Scanner;
import java.util.ArrayList;

public class UserInterface {
    
    private Scanner scanner;
    private ArrayList<Recipe> recipeList = new ArrayList<>();
    
    public UserInterface(Scanner scanner) {
        this.scanner = scanner;
    }
    
    public void start() {
        System.out.println("File to read: ");
        String holder = scanner.nextLine();
        readFile(holder);
        System.out.println("\nCommands: \nlist - lists the recipes \nstop - stops the program "
                + "\nfind name - searches recipes by name \nfind cooking time - searches recipes by cooking time"
                + "\nfind ingredient - searches recipes by ingredient");
        
        while (true) {
            System.out.println("\nEnter Command: ");
            String command = scanner.nextLine().toLowerCase();
            if (command.equals("stop")) {
                break;
            } else if (command.equals("list")) {
                System.out.println("\nRecipes: ");
                for (Recipe r: this.recipeList) {
                    System.out.println(r);
                }
                
            } else if (command.equals("find name")) {
                System.out.println("\nSearched word:");
                String word = scanner.nextLine();
                for (Recipe r: this.recipeList) {
                    if (r.getName().contains(word)) {
                        System.out.println(r);
                    }
                }
                
            } else if (command.equals("find cooking time")) {
                System.out.println("\nMax cooking time: ");
                int time = Integer.valueOf(scanner.nextLine());
                for (Recipe r: this.recipeList) {
                    if (r.getTime() <= time) {
                        System.out.println(r);
                    }
                }
                
            } else if (command.equals("find ingredient")) {
                System.out.println("\nIngredient: ");
                String ingredient = scanner.nextLine();
                for (Recipe r: this.recipeList) {
                    if (r.getIngredients().contains(ingredient)) {
                        System.out.println(r);
                    }
                }   
            }
        }
    }
    
    public void readFile(String fileName) {
        
        try (Scanner fileReader = new Scanner(Paths.get(fileName))) {
            
            while (fileReader.hasNextLine()) {
                String line = fileReader.nextLine();
                if (line.isEmpty()) {
                    continue;
                }
                String name = line;
                
                int time = Integer.valueOf(fileReader.nextLine());
                
                ArrayList<String> things = new ArrayList();
                
                while (fileReader.hasNextLine()) {
                    String ingredient = fileReader.nextLine();
                    if (ingredient.isEmpty()) {
                        break;
                    }
                    things.add(ingredient);
                }
                recipeList.add(new Recipe(name, time, things));
            }
        }catch (Exception e) {
            System.out.println(e);
        }
    }
}
