import java.io.*;
import java.util.*;

public class Main {
    static int toSec(String t) {
        String[] p = t.split(":");
        int h = Integer.parseInt(p[0]);
        int m = Integer.parseInt(p[1]);
        int s = Integer.parseInt(p[2]);
        return h * 3600 + m * 60 + s;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        int[] dep = new int[m];

        for (int i = 0; i < n; i++) arr[i] = toSec(br.readLine().trim());
        for (int i = 0; i < m; i++) dep[i] = toSec(br.readLine().trim());

        int sMin = Integer.parseInt(br.readLine().trim());

        int ans = Integer.MAX_VALUE;
        for (int a : arr) {
            for (int d : dep) {
                int diff = d - a;
                if (diff >= sMin) {
                    ans = Math.min(ans, diff);
                }
            }
        }

        System.out.println(ans == Integer.MAX_VALUE ? -1 : ans);
    }
}