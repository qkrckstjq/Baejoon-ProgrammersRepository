import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = rd.readLine().split(" ");
        int n = Integer.parseInt(NM[0]);
        int m = Integer.parseInt(NM[1]);
        
        int[][] board = new int[n][m];
        for(int i = 0; i < n; i++) {
            String[] row = rd.readLine().split(" ");
            board[i] = Arrays.stream(row).mapToInt(Integer::parseInt).toArray();
        }
        int k = Integer.parseInt(rd.readLine());
        for(int i = 0; i < k; i++) {
            String[] row = rd.readLine().split(" ");
            int result = 0;
            int[] ijxy = Arrays.stream(row).mapToInt(Integer::parseInt).toArray();
            for(int j = ijxy[0] - 1; j <= ijxy[2] - 1; j++) {
                for(int q = ijxy[1] - 1; q <= ijxy[3] - 1; q++) {
                    result += board[j][q];
                }
            }
            System.out.println(result);
        }
    }
}