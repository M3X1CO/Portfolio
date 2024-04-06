/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */

import java.util.*;

public class UserInterface {
    
    private Scanner scanner;
    private ArrayList<Bird> birds = new ArrayList<>();
    
    public UserInterface(Scanner scanner) {
        this.scanner = scanner;
    }
    
    public void start() {
        // run the main loop
        
        while (true) {
            System.out.println("?");
            String command = scanner.nextLine();
            
            if (command.equals("Quit")) {
                break;
            }
            
            if (command.equals("Add")) {
                System.out.println("Name: ");
                String name = scanner.nextLine();
                System.out.println("Name in Latin: ");
                String latinName = scanner.nextLine();
                birds.add(new Bird(name, latinName));
                continue;
                
            } else if (command.equals("Observation")) {
                System.out.println("Bird? ");
                String named = scanner.nextLine();
                
                for (Bird b: this.birds) {
                    if (b.getName().contains(named)) {
                        b.addObs();
                        System.out.println(b);
                    } else {
                        System.out.println("Not a bird!");
                    }
                }
                continue;
                                
            } else if (command.equals("All")) {
                for (Bird b: this.birds) {
                    System.out.println(b);
                }
                continue;
                
            } else if (command.equals("One")) {
                System.out.println("Bird: ");
                String tamed = scanner.nextLine();
                
                for (Bird b: this.birds) {
                    if (b.getName().contains(tamed)) {
                        System.out.println(b);
                    }
                }
            }
        }
        
    }
}
