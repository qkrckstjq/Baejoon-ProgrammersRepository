import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] ans = new int[1001];
        for (int n = 1; n <= 1000; n++) {
            int sum = 0;
            for (int b = 2; b <= n; b++) {
                int x = n;
                while (x % b == 0) { sum++; x /= b; }
            }
            ans[n] = sum;
        }

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            sb.append(ans[n]).append('\n');
        }
        System.out.print(sb);
    }
}
