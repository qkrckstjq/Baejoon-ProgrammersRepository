import java.io.*;

public class Main {
    static boolean okHour(int x) { return 1 <= x && x <= 12; }
    static boolean okMinSec(int x) { return 0 <= x && x <= 59; }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] sp = br.readLine().split(":");
        int[] t = new int[3];
        for (int i = 0; i < 3; i++) t[i] = Integer.parseInt(sp[i]);

        int cnt = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (i == j || j == k || i == k) continue;
                    int h = t[i], m = t[j], s = t[k];
                    if (okHour(h) && okMinSec(m) && okMinSec(s)) cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}
