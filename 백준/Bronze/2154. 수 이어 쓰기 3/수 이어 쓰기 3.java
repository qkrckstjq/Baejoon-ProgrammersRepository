import java.io.*;
import java.util.*;

public class Main {
    static int[] prefix(char[] p) {
        int m = p.length;
        int[] pi = new int[m];
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && p[i] != p[j]) j = pi[j - 1];
            if (p[i] == p[j]) pi[i] = ++j;
        }
        return pi;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        char[] p = Integer.toString(n).toCharArray();
        int m = p.length;
        int[] pi = prefix(p);

        char[] buf = new char[10];

        int j = 0;
        int pos = 0;

        for (int x = 1; x <= n; x++) {
            int t = x;
            int idx = 10;
            while (t > 0) {
                buf[--idx] = (char) ('0' + (t % 10));
                t /= 10;
            }
            for (int k = idx; k < 10; k++) {
                char c = buf[k];
                pos++;

                while (j > 0 && c != p[j]) j = pi[j - 1];
                if (c == p[j]) j++;

                if (j == m) {
                    System.out.println(pos - m + 1);
                    return;
                }
            }
        }
    }
}
