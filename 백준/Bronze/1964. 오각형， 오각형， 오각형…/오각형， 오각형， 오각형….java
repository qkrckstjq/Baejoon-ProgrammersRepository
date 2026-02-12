import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final long MOD = 45678L;

        long n = Long.parseLong(br.readLine());

        long a = n;
        long b = 3L * n + 5L;

        if ((a & 1L) == 0L) a /= 2L;
        else b /= 2L;

        long ans = ((a % MOD) * (b % MOD)) % MOD;
        ans = (ans + 1L) % MOD;

        System.out.println(ans);
    }
}