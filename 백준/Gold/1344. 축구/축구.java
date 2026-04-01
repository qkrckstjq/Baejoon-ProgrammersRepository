import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    static final int[] PRIMES = {2, 3, 5, 7, 11, 13, 17};
    static long[] comb = new long[19];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        double a = Double.parseDouble(br.readLine()) / 100.0;
        double b = Double.parseDouble(br.readLine()) / 100.0;

        comb[0] = 1;
        for (int i = 1; i <= 18; i++) {
            comb[i] = comb[i - 1] * (18 - i + 1) / i;
        }

        double aPrime = primeGoalProb(a);
        double bPrime = primeGoalProb(b);

        double answer = 1.0 - (1.0 - aPrime) * (1.0 - bPrime);
        System.out.println(answer);
    }

    static double primeGoalProb(double p) {
        double result = 0.0;

        for (int k : PRIMES) {
            result += comb[k] * Math.pow(p, k) * Math.pow(1.0 - p, 18 - k);
        }

        return result;
    }
}