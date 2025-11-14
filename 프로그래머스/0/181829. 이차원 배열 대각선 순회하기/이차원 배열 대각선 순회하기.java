class Solution {
    public int solution(int[][] board, int k) {
        int answer = 0;
        for(int i = 0; i <= k; i++) {
            if(i < board.length) {
                for(int j = 0; j <= k; j++) {
                    if(j < board[i].length) {
                        if(i + j <= k) answer += board[i][j];
                        if(i + j > k) break;    
                    }
                }   
            }
        }
        return answer;
    }
}