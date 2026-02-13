import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] g = new char[R][C];
        for (int i = 0; i < R; i++) {
            g[i] = br.readLine().toCharArray();
        }

        int[] ans = new int[5];

        for (int i = 0; i < R - 1; i++) {
            for (int j = 0; j < C - 1; j++) {
                boolean blocked = false;
                int crushed = 0;

                for (int di = 0; di < 2; di++) {
                    for (int dj = 0; dj < 2; dj++) {
                        char c = g[i + di][j + dj];
                        if (c == '#') blocked = true;
                        else if (c == 'X') crushed++;
                    }
                }

                if (!blocked) ans[crushed]++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int k = 0; k <= 4; k++) sb.append(ans[k]).append('\n');
        System.out.print(sb.toString());
    }
}