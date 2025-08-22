class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] board = new int[rows][columns];
        int v = 1;
        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < columns; j++) {
                board[i][j] = v++;
            }
        }
        
        for(int i = 0; i < queries.length; i++) {
            int[] command = queries[i];
            int y1 = command[0] - 1;
            int x1 = command[1] - 1;
            int y2 = command[2] - 1;
            int x2 = command[3] - 1;
            
            
            int prev = board[y1 + 1][x1];
            int minNum = prev;
            for(int x = x1; x <= x2; x++) {
                int temp = board[y1][x];
                board[y1][x] = prev;
                prev = temp;
                minNum = Math.min(minNum, board[y1][x]);
            }
            
            for(int y = y1 + 1; y <= y2; y++) {
                int temp = board[y][x2];
                board[y][x2] = prev;
                prev = temp;
                minNum = Math.min(minNum, board[y][x2]);
            }
            
            for(int x = x2 - 1; x >= x1; x--) {
                int temp = board[y2][x];
                board[y2][x] = prev;
                prev = temp;
                minNum = Math.min(minNum, board[y2][x]);
            }
            
            for(int y = y2 - 1; y >= y1; y--) {
                int temp = board[y][x1];
                board[y][x1] = prev;
                prev = temp;
                minNum = Math.min(minNum, board[y][x1]);
            }
            answer[i] = minNum;
        }
        
        
        return answer;
    }
}