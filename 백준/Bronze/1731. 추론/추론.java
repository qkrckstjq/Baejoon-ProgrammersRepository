import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());
        long[] a = new long[n];

        for (int i = 0; i < n; i++) {
            a[i] = Long.parseLong(br.readLine().trim());
        }

        long d1 = a[1] - a[0];
        long d2 = a[2] - a[1];

        long ans;
        if (d1 == d2) {
            ans = a[n - 1] + d1;
        } else {
            long r = a[1] / a[0];
            ans = a[n - 1] * r;
        }

        System.out.println(ans);
    }
}