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

public class IOU {
    private HashMap<String, Double> iou;
    
    public IOU() {
        this.iou = new HashMap<>();
    }
    
    public void setSum(String toWhom, double amount) {
        iou.put(toWhom, amount);
    }
    
    public double howMuchDoIOweTo(String toWhom) {
        Double dousyDay = 0.0;
        for (String key : iou.keySet()) {
            if (key.contains(toWhom)) {
                dousyDay = iou.get(key);
            }
        }
        return dousyDay;
    }
}
