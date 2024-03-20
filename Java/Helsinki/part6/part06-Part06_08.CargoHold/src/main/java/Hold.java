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

public class Hold {
    private int weight;
    private ArrayList<Suitcase> suitcases;
    
    public Hold(int weight) {
        this.weight = weight;
        this.suitcases = new ArrayList<>();
    }
    
    public void addSuitcase(Suitcase suitcase) {
        if (maxWeight() + suitcase.totalWeight() <= weight) {
            suitcases.add(suitcase);
        }
    }
    
    public int maxWeight() {
        int totWeight = 0;
        for (Suitcase name: suitcases) {
            totWeight += name.totalWeight();
        }
        return totWeight;
    }
    
    public String toString() {
        return suitcases.size() + " suitcases (" + maxWeight() + " kg)";
    }
    
    public void printItems() {
        for (Suitcase suitcase: suitcases) {
            suitcase.printItems();
        }
    }
}
