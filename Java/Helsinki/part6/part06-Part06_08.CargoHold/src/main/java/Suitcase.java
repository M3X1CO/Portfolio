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

public class Suitcase {
    private int maxWeight;
    private int totWeight;
    private ArrayList<Item> items;
    
    public Suitcase(int maxWeight) {
        this.maxWeight = maxWeight;
        this.totWeight = 0;
        this.items = new ArrayList<>();
    }
    
    public void addItem(Item item) {
        if (item.getWeight() + totWeight <= maxWeight) {
            items.add(item);
            totWeight += item.getWeight();
        }
    }
    
    public String toString() {
        if (items.isEmpty()) {
            return "no items (" + totWeight + " kg)";
        }
        
        if (items.size() == 1) {
            return items.size() + " item (" + this.totWeight + " kg)";
        } else {
            return items.size() + " items (" + this.totWeight + " kg)";
        }
    }
    
    public void printItems() {
        // System.out.println("The suitcase contains the following items:");
 
        for (Item item: items) {
            System.out.println(item.getName() + " (" + item.getWeight() + " kg)");
        }
    }
    
    public int totalWeight() {
        return totWeight;
    }
    
    public Item heaviestItem() {
        Item name = null;
        int heaviest = 0;
        for (Item item: items) {
            if (item.getWeight() > heaviest) {
                heaviest = item.getWeight();
                name = item;
            }
        }
        return name;
    }
}
