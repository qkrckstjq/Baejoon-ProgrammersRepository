import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[] cnt = new int[101];
        int maxT = 0;

        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            int in = Integer.parseInt(st.nextToken());
            int out = Integer.parseInt(st.nextToken());
            maxT = Math.max(maxT, out);

            for (int t = in; t < out; t++) cnt[t]++;
        }

        int sum = 0;
        for (int t = 0; t < maxT; t++) {
            if (cnt[t] == 1) sum += A;
            else if (cnt[t] == 2) sum += 2 * B;
            else if (cnt[t] == 3) sum += 3 * C;
        }

        System.out.println(sum);
    }
}