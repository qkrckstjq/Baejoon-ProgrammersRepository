import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        boolean[][] a = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine().trim();
            if (line.indexOf(' ') >= 0) {
                String[] parts = line.split("\\s+");
                for (int j = 0; j < m; j++) {
                    a[i][j] = parts[j].charAt(0) == '1';
                }
            } else {
                for (int j = 0; j < m; j++) {
                    a[i][j] = line.charAt(j) == '1';
                }
            }
        }

        int cnt = 0;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (a[i][j]) {
                    cnt++;
                    for (int x = 0; x <= i; x++) {
                        for (int y = 0; y <= j; y++) {
                            a[x][y] = !a[x][y];
                        }
                    }
                }
            }
        }

        System.out.println(cnt);
    }
}