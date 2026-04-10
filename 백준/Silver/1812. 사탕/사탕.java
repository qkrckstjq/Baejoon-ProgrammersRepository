import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] s = new int[n];
        
        for (int i = 0; i < n; i++) {
            s[i] = Integer.parseInt(br.readLine());
        }

        int[] a = new int[n];

        int sum = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) sum += s[i];
            else sum -= s[i];
        }

        a[0] = sum / 2;

        for (int i = 1; i < n; i++) {
            a[i] = s[i - 1] - a[i - 1];
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(a[i]).append('\n');
        }

        System.out.print(sb);
    }
}