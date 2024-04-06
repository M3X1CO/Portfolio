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

public class VehicleRegistry {
    private HashMap<LicensePlate, String> registry;
    
    public VehicleRegistry() {
        this.registry = new HashMap<>();
    }
    
    public boolean add(LicensePlate licensePlate, String owner) {
        if (registry.containsKey(licensePlate)) {
            return false;
        } else {
            registry.put(licensePlate, owner);
            return true;
        }
    }
    
    public String get(LicensePlate licensePlate) {
        return registry.get(licensePlate);
    }
    
    public boolean remove(LicensePlate licensePlate) {
        if (registry.containsKey(licensePlate)) {
            registry.remove(licensePlate);
            return true;
        } else {
            return false;
        }
    }
    
    public void printLicensePlates() {
        for (LicensePlate key : registry.keySet()) {
            System.out.println(key);
        }
    }
    
    public void printOwners() {
        HashSet<String> ownersPrinted = new HashSet<>();
        for (String owner : registry.values()) {
            if (!ownersPrinted.contains(owner)) {
                System.out.println(owner);
                ownersPrinted.add(owner);
            }
        }
    }
}
