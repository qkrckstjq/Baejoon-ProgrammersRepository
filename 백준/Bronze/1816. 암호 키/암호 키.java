import java.io.*;
import java.util.*;

public class Main {
    static final int LIMIT = 1000000;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        List<Integer> primes = getPrimes(LIMIT);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            long s = Long.parseLong(br.readLine());
            boolean safe = true;

            for (int p : primes) {
                if (s % p == 0) {
                    safe = false;
                    break;
                }
            }

            sb.append(safe ? "YES" : "NO").append('\n');
        }

        System.out.print(sb);
    }

    static List<Integer> getPrimes(int limit) {
        boolean[] isComposite = new boolean[limit + 1];
        List<Integer> primes = new ArrayList<>();

        for (int i = 2; i * i <= limit; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isComposite[j] = true;
                }
            }
        }

        for (int i = 2; i <= limit; i++) {
            if (!isComposite[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}