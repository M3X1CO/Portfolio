/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */
public class PaymentCard {
    private double balance;
    
    public PaymentCard(double openingBalance) {
        // write code here
        this.balance = openingBalance;
    }
    
    public String toString() {
        // return print ready code here
        return "The card has a balance of " + this.balance + " euros";
    }
    
    public void eatAffordably() {
        // eat out of the garbage
        if (this.balance - 2.60 >= 0) {
            this.balance -= 2.60;
        }
    }
    
    public void eatHeartily() {
        // can afford the dollar menu at mcdonalds!
        if (this.balance - 4.60 >= 0) {
            this.balance -= 4.60;
        }
    }
    
    public void addMoney(double amount) {
        // tax return mfers!
        if (amount < 0){
            return;
        }
        else if (this.balance + amount <= 150) {
            this.balance += amount;
        } else {
            this.balance = 150;
        }
    }
}
