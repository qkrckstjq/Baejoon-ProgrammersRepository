import java.util.*;

class Solution {
    public int solution(int[][] triangle) {
        if(triangle.length == 1){
            return triangle[0][0];
        }
        int answer = 0;
        
        // int[][] board = new int[triangle.length][triangle.length];
        // board[0][0] = triangle[0][0];
        
        for(int i = 1; i < triangle.length; i++) {
            for(int j = 0; j <= i; j++) {
                int cur = triangle[i][j];
                int ul = j > 0 ? triangle[i - 1][j - 1] + cur : 0;
                int ur = j < i ? triangle[i - 1][j] + cur : 0;
                triangle[i][j] = Math.max(ul, ur);
                // if(i == triangle.length - 1) {
                //     answer = Math.max(answer, triangle[i][j]);
                // }
            }
        }
        for(int num : triangle[triangle.length - 1]) {
            answer = Math.max(answer, num);
        }

        return answer;
    }
}