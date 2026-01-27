import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        int[] prefix = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(br.readLine().trim());
            prefix[i] = sum;
        }

        StringBuilder out = new StringBuilder();
        for (int i = 0; i < q; i++) {
            int t = Integer.parseInt(br.readLine().trim());
            int lo = 0, hi = n - 1;
            while (lo < hi) {
                int mid = (lo + hi) >>> 1;
                if (t < prefix[mid]) hi = mid;
                else lo = mid + 1;
            }
            out.append(lo + 1).append('\n');
        }

        System.out.print(out.toString());
    }
}
