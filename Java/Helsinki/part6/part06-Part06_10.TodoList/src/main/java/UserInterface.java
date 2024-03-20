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
    private final TodoList todoList;
    private final Scanner scanner;

    public UserInterface(TodoList todoList, Scanner scanner) {
        this.todoList = todoList;
        this.scanner = scanner;
    }

    public void start() {
        while (true) {
            System.out.println("Command: ");
            String command = scanner.nextLine().toLowerCase().trim();
            
            if (command.equals("stop")) {
                break;
            } else if (command.equals("add")) {
                System.out.println("To add: ");
                String newPhrase = scanner.nextLine();
                todoList.add(newPhrase);
            } else if (command.equals("list")) {
                todoList.print();
            } else if (command.equals("remove")) {
                System.out.println("Which one is removed? ");
                int index = Integer.valueOf(scanner.nextLine());

                todoList.remove(index);
            }
        }
    }
}
