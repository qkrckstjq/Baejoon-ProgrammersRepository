import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] first = br.readLine().trim().split(" ");
        int N = Integer.parseInt(first[0]);
        int K = Integer.parseInt(first[1]);

        String[] parts = br.readLine().trim().split(",");
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(parts[i]);

        int len = N;
        for (int step = 0; step < K; step++) {
            for (int i = 0; i < len - 1; i++) {
                arr[i] = arr[i + 1] - arr[i];
            }
            len--;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++) {
            if (i > 0) sb.append(",");
            sb.append(arr[i]);
        }
        System.out.print(sb.toString());
    }
}