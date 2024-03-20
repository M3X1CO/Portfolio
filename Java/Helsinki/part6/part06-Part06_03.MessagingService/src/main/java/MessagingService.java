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

public class MessagingService {
    private ArrayList<Message> messages;
    
    public MessagingService() {
        this.messages = new ArrayList<>();
    }
    
    public void add(Message message) {
        // Check if the message content is at most 280 characters long
        if (message.getContent().length() <= 280) {
            this.messages.add(message);
        }
    }
    
    public ArrayList<Message> getMessages() {
        return new ArrayList<>(this.messages);
    }
}
