/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */
public class Objects {
    private String identifier;
    private String name;
    
    public Objects(String identifier, String name) {
        this.identifier = identifier;
        this.name = name;
    }
    
    public String getName() {
        return this.name;
    }
    
    public String getIdentifier() {
        return this.identifier;
    }
    
    public boolean equals(Object compared) {
        if (this == compared) {
            return true;
        }
        if (!(compared instanceof Objects)) {
            return false;
        }
        Objects compareCollection = (Objects) compared;
        return this.identifier.equals(compareCollection.identifier);
    }
    
    public String toString() {
        return this.identifier + ": " + this.name;
    }
}
