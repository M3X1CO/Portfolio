
import java.util.ArrayList;

public class GradeRegister {

    private ArrayList<Integer> grades;
    private ArrayList<Integer> register;

    public GradeRegister() {
        this.grades = new ArrayList<>();
        this.register = new ArrayList<>();
    }

    public void addGradeBasedOnPoints(int points) {
        this.grades.add(pointsToGrade(points));
        register.add(points);
    }

    public int numberOfGrades(int grade) {
        int count = 0;
        for (int received : this.grades) {
            if (received == grade) {
                count++;
            }
        }

        return count;
    }

    public static int pointsToGrade(int points) {

        int grade = 0;
        if (points < 50) {
            grade = 0;
        } else if (points < 60) {
            grade = 1;
        } else if (points < 70) {
            grade = 2;
        } else if (points < 80) {
            grade = 3;
        } else if (points < 90) {
            grade = 4;
        } else {
            grade = 5;
        }

        return grade;
    }
    
    public double averageOfGrades() {
        int sumNum = 0;
        int count = 0;
        
        if (grades.isEmpty()) {
            return -1;
        }
        
        for (int grad: grades) {
            sumNum += grad;
            count++;
        }
        return (double) sumNum / count;
    }
    
    public double averageOfPoints() {
        int sumNum = 0;
        int count = 0;
                
        if (register.isEmpty()) {
            return -1;
        }
        
        for (int reg: register) {
            sumNum += reg;
            count++;
        }
        
        return (double) sumNum / count;
    }
}
