import java.io.*;
import java.util.*;

class Main {
    public static int[] dy = new int[]{0, 0, 1, -1};
    public static int[] dx = new int[]{1, -1, 0, 0};
    
    public static void main(String[] args) throws Exception {
        BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = rd.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);
        String[][] board = new String[n][m];
        
        for(int i = 0; i < n; i++) {
            board[i] = rd.readLine().split("");
        }
        
        boolean[][] visit = new boolean[n][m];
        int answer = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(!visit[i][j]) {
                    // System.out.printf("%d,,%d\n",i,j);
                    dfs(i, j, visit, board);
                    answer += 1;
                }
            }
        }
        System.out.println(answer);
    }
    
    public static void dfs(int y, int x, boolean[][] visit, String[][] board) {
        int[] arr = new int[2];
        if(board[y][x].equals("-")) {
            arr[0] = 0;
            arr[1] = 1;
        } else {
            arr[0] = 2;
            arr[1] = 3;
        }
        List<int[]> stack = new ArrayList<>();
        stack.add(new int[]{y, x});
        while(!stack.isEmpty()) {
            int[] curYX = stack.get(stack.size() - 1);
            stack.remove(stack.size() - 1);
            int curY = curYX[0];
            int curX = curYX[1];
            visit[curY][curX] = true;
            
            for(int i = 0; i < 2; i++) {
                int nextY = curY + dy[arr[i]];
                int nextX = curX + dx[arr[i]];
                if(0 <= nextY && nextY < visit.length && 0 <= nextX && nextX < visit[0].length) {
                    if(!visit[nextY][nextX] && board[nextY][nextX].equals(board[y][x])) {
                        stack.add(new int[]{nextY, nextX});
                    }
                }
            }
        }
    }
}