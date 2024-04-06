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

public class StorageFacility {
    private HashMap<String, ArrayList<String>> storage;
    
    public StorageFacility() {
        this.storage = new HashMap<>();
    }
    
    public void add(String unit, String item) {
        storage.putIfAbsent(unit, new ArrayList<>());
        ArrayList<String> items = storage.get(unit);
        items.add(item);
    }
    
    public ArrayList<String> contents(String storageUnit) {
        return storage.getOrDefault(storageUnit, new ArrayList<>());
    }
    
    public void remove(String storageUnit, String item) {
        ArrayList<String> items = storage.get(storageUnit);
        if (items != null) {
            items.remove(item);
            if (items.isEmpty()) {
                storage.remove(storageUnit);
            }
        }
    }
    
    public ArrayList<String> storageUnits() {
        ArrayList<String> unitsWithItems = new ArrayList<>();
        for (Map.Entry<String, ArrayList<String>> entry : storage.entrySet()) {
            if (!entry.getValue().isEmpty()) {
                unitsWithItems.add(entry.getKey());
            }
        }
        return unitsWithItems;
    }
}
