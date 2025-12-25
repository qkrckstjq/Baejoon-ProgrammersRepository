import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(br.readLine().trim());

        long p = 10;
        while (n >= p) {
            long r = n % p;        
            long half = p / 2;     

            if (r >= half) n = n - r + p; 
            else n = n - r;               

            p *= 10;
        }

        System.out.println(n);
    }
}