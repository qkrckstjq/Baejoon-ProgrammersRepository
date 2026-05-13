class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        
        int[][] board = new int[n][m];
        boolean[][] water = new boolean[n][m];
        
        board[0][0] = 1;
        
        for(int[] w : puddles) {
            water[w[1] - 1][w[0] - 1] = true;
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(i == 0 && j == 0) continue;
                if(water[i][j]) continue;
                
                long up = i > 0 ? board[i - 1][j] : 0;
                long left = j > 0 ? board[i][j - 1] : 0;

                board[i][j] = (int)((up + left) % 1000000007);
            }
        }
    
        return board[n - 1][m - 1];
    }
}