import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        long n = Long.parseLong(rd.readLine());
        long answer = 1;
        long mod = 1_000_000_000_000L;
        for(long i = n; i > 0; i--) {            
            answer *= i;
            while(answer / 10 * 10 == answer) {
                answer /= 10;
            }
            answer %= mod;
        }
        answer %= 100000;
        System.out.println("0".repeat(5 - Long.toString(answer).length()) + Long.toString(answer));
    }
}