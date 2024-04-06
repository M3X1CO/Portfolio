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
    private TodoList list;
    
    public UserInterface(TodoList list, Scanner scanner) {
        this.scanner = scanner;
        this.list = list;        
    }
    
    public void start() {
        
        while (true) {
            System.out.println("Command: ");
            String input = scanner.nextLine();
            if (input.equals("stop")) {
                break;
            }
            
            if (input.equals("add")) {
                System.out.println("To add: ");
                String toAdd = scanner.nextLine();
                this.list.add(toAdd);
            } else if (input.equals("list")) {
                this.list.print();
            } else if (input.equals("remove")) {
                System.out.println("Which one is removed? ");
                int toRemove = Integer.valueOf(scanner.nextLine());
                this.list.remove(toRemove);
            } else {
                continue;
            }
        }
    }
}
