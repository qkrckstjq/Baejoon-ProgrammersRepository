import java.util.*;
import java.math.BigInteger;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String bin = sc.nextLine();
        BigInteger value = new BigInteger(bin, 2);  
        String oct = value.toString(8);             

        System.out.println(oct);
    }
}