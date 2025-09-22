import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] NM = makeIntArray(reader.readLine().split(" "));
        int N = NM[0], M = NM[1];

        int[][] A = new int[N][M];
        int[][] B = new int[N][M];

        // 첫 번째 행렬
        for (int i = 0; i < N; i++) {
            A[i] = makeIntArray(reader.readLine().split(" "));
        }

        // 두 번째 행렬
        for (int i = 0; i < N; i++) {
            B[i] = makeIntArray(reader.readLine().split(" "));
        }

        // 행렬 덧셈
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(A[i][j] + B[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.print(sb);
    }

    public static int[] makeIntArray(String[] array) {
        return Arrays.stream(array).mapToInt(Integer::parseInt).toArray();
    }
}