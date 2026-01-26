import java.io.*;
import java.util.*;

public class Main {

    static long dist2(int x1, int y1, int x2, int y2) {
        long dx = (long) x1 - x2;
        long dy = (long) y1 - y2;
        return dx * dx + dy * dy;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            int[] x = new int[4];
            int[] y = new int[4];

            for (int i = 0; i < 4; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                x[i] = Integer.parseInt(st.nextToken());
                y[i] = Integer.parseInt(st.nextToken());
            }

            long[] d = new long[6];
            int idx = 0;
            for (int i = 0; i < 4; i++) {
                for (int j = i + 1; j < 4; j++) {
                    d[idx++] = dist2(x[i], y[i], x[j], y[j]);
                }
            }

            Arrays.sort(d);

            boolean ok = d[0] > 0
                    && d[0] == d[1] && d[1] == d[2] && d[2] == d[3]
                    && d[4] == d[5]
                    && d[4] == 2 * d[0];

            out.append(ok ? 1 : 0).append('\n');
        }

        System.out.print(out.toString());
    }
}
