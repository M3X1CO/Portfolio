/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Howar
 */
public class Timer {
    private ClockHand hundredths;
    private ClockHand seconds;
    
    public Timer() {
        this.hundredths = new ClockHand(100);
        this.seconds = new ClockHand(60);
    }
    
    public String toString() {
        return String.format("%02d:%02d", seconds.value(), hundredths.value());
    }
    
    public void advance() {
        hundredths.advance();
        if (hundredths.value() == 0) {
            seconds.advance();
        }
    }
    
    public static void main (String[] args) {
        Timer timer = new Timer();
        
        while (true) {
            System.out.println(timer);
            timer.advance();
            
            try {
                Thread.sleep(10);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}


