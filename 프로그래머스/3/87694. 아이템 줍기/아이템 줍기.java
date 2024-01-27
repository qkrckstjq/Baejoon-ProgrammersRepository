import java.util.*;

// System.out.println(maxX);
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        LinkedList<Integer[]> queue = new LinkedList<>();
        int maxY = 0;
        int maxX = 0;
        int[] moveY = {0,0,1,-1};
        int[] moveX = {1,-1,0,0};
        
        for(int i = 0; i < rectangle.length; i++) {
            maxY = maxY <= rectangle[i][3] ? rectangle[i][3] : maxY;
            maxX = maxX <= rectangle[i][2] ? rectangle[i][2] : maxX;
        }
        Integer[] startPoint = {characterY*2, characterX*2, 0};
        boolean[][] visit = new boolean[maxY*2+1][maxX*2+1];
        queue.add(startPoint);
        
        while(!queue.isEmpty()) {
            Integer[] cur = queue.poll();
            int curY = cur[0];
            int curX = cur[1];
            int curK = cur[2];
            visit[curY][curX] = true;
            if(curY == itemY*2 && curX == itemX*2) {
                return curK/2;
            }
            for(int i = 0; i < moveY.length; i++) {
                int nextY = curY + moveY[i];
                int nextX = curX + moveX[i];
                int nextK = curK + 1;
                if(isExist(nextY, nextX, rectangle) && !isDuplicate(nextY, nextX, rectangle) && !visit[nextY][nextX]) {
                    Integer[] temp = {nextY, nextX, nextK};
                    queue.add(temp);
                }
            }
        }
        return -1;
    }
    //[1,2,7,5]
    //y의 범위 1 ~ 5 i = 1, i = 3
    //x의 범위 1 ~ 7 i = 0, i = 2
    
    public boolean isExist (int y, int x, int[][] A) {
        for(int i = 0; i < A.length; i++) {
            if( ((x == A[i][0]*2 || x == A[i][2]*2) && A[i][1]*2 <= y && y <= A[i][3]*2) || 
               ((y == A[i][1]*2 || y == A[i][3]*2) && A[i][0]*2 <= x && x <= A[i][2]*2))
            {
                return true;
            }
        }
        return false;
    }
    
    public boolean isDuplicate (int y, int x, int[][] A) {
        for(int i = 0; i < A.length; i++) {
            if(A[i][1]*2 < y && y < A[i][3]*2 && A[i][0]*2 < x && x < A[i][2]*2) {
                return true;
            }
        }
        return false;
    }
    
}