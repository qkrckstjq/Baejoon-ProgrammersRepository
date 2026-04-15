import java.io.*;
import java.util.*;
import java.math.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String input = rd.readLine();        
        BigInteger bI = new BigInteger(input);
        int mod = 1000000;
        BigInteger period = new BigInteger("1500000");
        int n = bI.remainder(period).intValue();
        if(n == 0) {
            System.out.println(0);
            return;
        }
        int prev = 0;
        int answer = 1;
        for(int i = 0; i < n - 1; i++) {
            int temp = answer;
            answer = (prev + answer) % mod;
            prev = temp;
        }
        System.out.println(answer);
    }
}