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

public class Room {
    private ArrayList<Person> room;
    
    public Room() {
        this.room = new ArrayList<>();
    }
    
    public void add(Person person) {
        room.add(person);
    }
    
    public boolean isEmpty() {
        return room.isEmpty();
    }
    
    public ArrayList<Person> getPersons() {
        return new ArrayList<>(room);
    }
    
    public Person shortest() {
        if (room.isEmpty()) {
            return null;
        }
        
        Person shortestPerson = room.get(0);
        for (Person person: room) {
            if (person.getHeight() < shortestPerson.getHeight()) {
                shortestPerson = person;
            }
        }
        return shortestPerson;
    }
    
    public Person take() {
        if (room.isEmpty()) {
            return null;
        }
        Person shortestPerson = shortest();
        room.remove(shortestPerson);
        return shortestPerson;
    }
}
