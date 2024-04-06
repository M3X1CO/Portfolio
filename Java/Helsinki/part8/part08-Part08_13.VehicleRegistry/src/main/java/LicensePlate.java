
import java.util.Objects;

public class LicensePlate {
    // don't modify existing parts of this class

    // these instance variables have been defined as final, meaning 
    // that once set, their value can't be changed
    private final String liNumber;
    private final String country;

    public LicensePlate(String country, String liNumber) {
        this.liNumber = liNumber;
        this.country = country;
    }

    @Override
    public String toString() {
        return country + " " + liNumber;
    }

    @Override
    public boolean equals(Object object) {
        if (this == object) {
            return true;
        }
        if (object == null || getClass() != object.getClass()) {
            return false;
        }
        LicensePlate other = (LicensePlate) object;
        return country.equals(other.country) && liNumber.equals(other.liNumber);
    }
    
    @Override
    public int hashCode() {
        int result = country.hashCode();
        result = 31 * result + liNumber.hashCode();
        return result;
    }
}
