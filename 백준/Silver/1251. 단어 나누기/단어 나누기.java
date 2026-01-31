import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int n = s.length();

        String best = null;

        for (int i = 1; i <= n - 2; i++) {
            for (int j = i + 1; j <= n - 1; j++) {
                String a = new StringBuilder(s.substring(0, i)).reverse().toString();
                String b = new StringBuilder(s.substring(i, j)).reverse().toString();
                String c = new StringBuilder(s.substring(j)).reverse().toString();
                String cand = a + b + c;

                if (best == null || cand.compareTo(best) < 0) best = cand;
            }
        }

        System.out.println(best);
    }
}
