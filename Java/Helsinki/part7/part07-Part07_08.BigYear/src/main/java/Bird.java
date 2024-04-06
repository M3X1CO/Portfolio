/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */
public class Bird {
    
    private String name;
    private String latinName;
    private int observations = 0;
    
    public Bird(String name, String latinName) {
        this.name = name;
        this.latinName = latinName;
    }
    
    public void addObs() {
        this.observations += 1;
    }
    
    public String getName() {
        return this.name;
    }
    
    public String getLatinName() {
        return this.latinName;
    }
    
    public int getObs() {
        return this.observations;
    }
    
    @Override
    public String toString() {
        return this.name + " (" + this.latinName + "): " + observations + " observations";
    }
}
