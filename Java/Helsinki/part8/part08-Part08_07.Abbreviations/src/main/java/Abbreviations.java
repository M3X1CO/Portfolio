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

public class Abbreviations {
    private HashMap<String, String> abbrev = new HashMap<>();
    
    public Abbreviations() {
        
    }
    
    public void addAbbreviation(String abbreviation, String explanation) {
        abbrev.put(abbreviation, explanation);
    }
    
    public boolean hasAbbreviation(String abbreviation) {
        if (abbrev.containsKey(abbreviation)) {
            return true;
        }
        return false;
    }
    
    public String findExplanationFor(String abbreviation) {
        if (abbrev.containsKey(abbreviation)) {
            return abbrev.get(abbreviation);
        }
        return null;
    }
}
