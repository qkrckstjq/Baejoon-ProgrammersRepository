import java.io.*;
import java.math.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        BigInteger a = new BigInteger(rd.readLine());
        BigInteger b = new BigInteger(rd.readLine());
        
        System.out.printf("%d\n%d\n%d", a.add(b), a.subtract(b), a.multiply(b));
    }
}