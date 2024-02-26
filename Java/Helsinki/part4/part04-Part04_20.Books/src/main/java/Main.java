import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        // implement here the program that allows the user to enter 
        // book information and to examine them
        
        Scanner scanner = new Scanner(System.in);
        ArrayList<Books> books = new ArrayList<>();
        
        while (true) {
            System.out.println("Title: ");
            String title = scanner.nextLine();
            if (title.isEmpty()) {
                break;
            }
            System.out.println("Pages: ");
            int pages = Integer.valueOf(scanner.nextLine());
            
            System.out.println("Publication year: ");
            int published = Integer.valueOf(scanner.nextLine());
            
            books.add(new Books(title, pages, published));
        }
        System.out.println("What information will be printed? ");
        String beans = scanner.nextLine().toLowerCase();
        if (beans.equals("everything")) {
            for (Books book: books) {
                System.out.println(book);
            }
        } else if (beans.equals("name")) {
            for (Books book: books) {
                System.out.println(book.getName());
            }
        } else if (beans.equals("pages")) {
            for (Books book: books) {
                System.out.println(book.getPages());
            }
        } else if (beans.equals("published")) {
            for (Books book: books) {
                System.out.println(book.getPublished());
            }
        }
    }
}
