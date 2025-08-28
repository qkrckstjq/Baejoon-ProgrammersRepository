import java.util.*;

class Solution {
    public int[] dy = {0, 0, 1, -1};
    public int[] dx = {1, -1, 0, 0};
    
    public int removed = 0;
    
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        char[][] board = new char[storage.length][storage[0].length()];
        
        for(int i = 0; i < storage.length; i++) {
            for(int j = 0; j < storage[0].length(); j++) {
                board[i][j] = storage[i].charAt(j);   
            }
        }
        
        for(String req : requests) {
            List<List<Integer>> stack = new ArrayList<>();
            
            if(req.length() == 1) {
                for(int i = 0; i < board.length; i++) {
                    for(int j = 0; j < board[0].length; j++) {
                        if(board[i][j] == req.charAt(0)) {
                            lifter(stack, board, i, j);
                        }
                    }
                }
                for(List<Integer> yx : stack) {
                    board[yx.get(0)][yx.get(1)] = ' ';
                    removed += 1;
                }           
                stack = new ArrayList<>();
            } else {
                for(int i = 0; i < board.length; i++) {
                    for(int j = 0; j < board[0].length; j++) {
                        if(board[i][j] == req.charAt(0)) {
                            removed += 1;
                            board[i][j] = ' ';
                        }
                    }
                }
            }
            // System.out.println(removed);
        }
        
        
        
        return ((board.length * board[0].length) - removed);
    }
    
    public void lifter(List<List<Integer>> temp, char[][] board, int y, int x) {
        int H = board.length, W = board[0].length;

        if (y == 0 || x == 0 || y == H - 1 || x == W - 1) {
            temp.add(List.of(y, x));
            return;
        }
        
        Deque<List<Integer>> stack = new ArrayDeque<>();
        stack.addLast(List.of(y, x));
        boolean[][] visited = new boolean[board.length][board[0].length];
        
        while (!stack.isEmpty()) {
            List<Integer> yx = stack.removeLast();
            int curY = yx.get(0);
            int curX = yx.get(1);
            
            for(int i = 0; i < 4; i++) {
                int nY = curY + dy[i];
                int nX = curX + dx[i];
                if(0 <= nY && nY < board.length && 0 <= nX && nX < board[0].length) {
                    if(board[nY][nX] == ' ' && !visited[nY][nX]) {
                        visited[nY][nX] = true;
                        stack.addLast(List.of(nY, nX));
                    }
                } else {
                    temp.add(List.of(y, x));
                    return;
                }
            }
        }
        return;
    }
}