import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int P = Integer.parseInt(br.readLine().trim());

        for (int tc = 0; tc < P; tc++) {
            String s = br.readLine().trim();
            int[] cnt = new int[8];

            for (int i = 0; i <= 37; i++) {
                int a = (s.charAt(i)     == 'H') ? 1 : 0;
                int b = (s.charAt(i + 1) == 'H') ? 1 : 0;
                int c = (s.charAt(i + 2) == 'H') ? 1 : 0;

                int idx = (a << 2) | (b << 1) | c; // 0..7
                cnt[idx]++;
            }
            for (int i = 0; i < 8; i++) {
                if (i > 0) out.append(' ');
                out.append(cnt[i]);
            }
            if (tc < P - 1) out.append('\n');
        }

        System.out.print(out.toString());
    }
}
