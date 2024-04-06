
import java.util.HashMap;

public class Nicknames {

    public static void main(String[] args) {
        // Do the operations required here!
        
        HashMap<String, String> Hashimoto = new HashMap<>();
        
        Hashimoto.put("mathew", "matt");
        Hashimoto.put("michael", "mix");
        Hashimoto.put("arthur", "artie");
        
        System.out.println(Hashimoto.get("mathew"));
    }
}
