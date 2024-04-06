/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */

import java.util.Scanner;

public class UserInterface {
    
    private Container containerOne;
    private Container containerTwo;
    private Scanner scanner;
    
    public UserInterface(Container containerOne, Container containerTwo, Scanner scanner) {
        this.containerOne = containerOne;
        this.containerTwo = containerTwo;
        this.scanner = scanner;
    }
    
    public void start() {
        
        while (true) {
            
            System.out.println("First: " + containerOne);
            System.out.println("Second: " + containerTwo);
            
            String input = scanner.nextLine();
            if (input.equals("quit")) {
                break;
            }
            
            String[] parts = input.split(" ");
            String command = parts[0];
            int amount = Integer.valueOf(parts[1]);
            

            
            if (command.equals("add")) {
                this.containerOne.add(amount);
            } else if (command.equals("move")) {
                if (this.containerOne.contains() - amount >= 0) {
                    this.containerOne.remove(amount);
                    this.containerTwo.add(amount);
                } else {
                    int moveBuffer = this.containerOne.contains();
                    this.containerOne.remove(moveBuffer);
                    this.containerTwo.add(moveBuffer);
                }
            } else if (command.equals("remove")) {
                this.containerTwo.remove(amount);
            }
        } 
    }
}
