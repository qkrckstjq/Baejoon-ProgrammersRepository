import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static boolean[][] A, B;

    static void flip(int x, int y) {
        for (int i = x; i < x + 3; i++) {
            for (int j = y; j < y + 3; j++) {
                A[i][j] = !A[i][j];
            }
        }
    }

    static boolean same() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (A[i][j] != B[i][j]) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        A = new boolean[N][M];
        B = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) A[i][j] = (s.charAt(j) == '1');
        }
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) B[i][j] = (s.charAt(j) == '1');
        }

        if (N < 3 || M < 3) {
            System.out.println(same() ? 0 : -1);
            return;
        }

        int cnt = 0;
        for (int i = 0; i <= N - 3; i++) {
            for (int j = 0; j <= M - 3; j++) {
                if (A[i][j] != B[i][j]) {
                    flip(i, j);
                    cnt++;
                }
            }
        }

        System.out.println(same() ? cnt : -1);
    }
}