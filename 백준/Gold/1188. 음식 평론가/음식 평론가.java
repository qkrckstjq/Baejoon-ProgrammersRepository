import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] input = rd.readLine().split(" ");
        long n = Long.parseLong(input[0]);
        long m = Long.parseLong(input[1]);
        
        System.out.println(m - gcd(n, m));
    }
    
    public static long gcd(long a, long b) {
        while(b > 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }
        
        return a;
    }
}