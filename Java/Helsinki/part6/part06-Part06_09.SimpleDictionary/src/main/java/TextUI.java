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

public class TextUI {
    private SimpleDictionary dictionary;
    private Scanner scanner;
    
    public TextUI(Scanner scanner, SimpleDictionary dictionary) {
        this.dictionary = dictionary;
        this.scanner = scanner;
    }
    
    public void start() {
        while (true) {
            System.out.println("Command: ");
            String word = scanner.nextLine();
            
            if (word.equals("end")) {
                System.out.println("Bye bye!");
                break;
            } else if (word.equals("add")) {
                System.out.println("Word: ");
                String newWord = scanner.nextLine();
                System.out.println("Translation: ");
                String translation = scanner.nextLine();
                dictionary.add(newWord, translation);
            } else if (word.equals("search")) {
                System.out.println("To be translated: ");
                String translatedWord = scanner.nextLine();
                String translation = dictionary.translate(translatedWord);
                if (translation != null) {
                    System.out.println("Translation: " + translation);
                } else {
                    System.out.println("Word " + translatedWord + " was not found");
                }
            } else {
                System.out.println("Unknown command");
            }
        }
    }
}
