import java.math.*;
import java.io.*;
import java.util.*;
class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        BigInteger cur = new BigInteger(rd.readLine());
        
        List<String> opList = new ArrayList<>();
        List<BigInteger> numList = new ArrayList<>();
       
        for(int i = 0; i < n - 1; i++) {
            String op = rd.readLine();
            BigInteger next = new BigInteger(rd.readLine());
            
            if(op.equals("*")) {
                cur = cur.multiply(next);
            } else if(op.equals("/")) {
                cur = floorDiv(cur, next);
            } else {
                opList.add(op);
                numList.add(cur);
                cur = next;
            }
        }
        numList.add(cur);
        BigInteger result = numList.get(0);
        for(int i = 0; i < opList.size(); i++) {
            String op = opList.get(i);
            BigInteger temp = numList.get(i + 1);
            if(op.equals("+")){
                result = result.add(temp);
            } else{
                result = result.subtract(temp);
            }
        }
        System.out.println(result.toString());
    }
    public static BigInteger floorDiv(BigInteger a, BigInteger b) {
        BigInteger[] qr = a.divideAndRemainder(b);
        BigInteger q = qr[0];
        BigInteger r = qr[1];

        if (!r.equals(BigInteger.ZERO) && a.signum() != b.signum()) {
            q = q.subtract(BigInteger.ONE);
        }
        return q;
    }
}