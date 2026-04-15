import java.io.*;
import java.util.*;
import java.math.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(rd.readLine());
        if(n == 0) {
            System.out.println(0);
            return;
        }
        BigInteger prev = new BigInteger("0");
        BigInteger answer = new BigInteger("1");
        for(int i = 0; i < n - 1; i++) {
            String temp = answer.toString();
            answer = prev.add(answer);
            prev = new BigInteger(temp);
        }
        System.out.println(answer.toString());
    }
}