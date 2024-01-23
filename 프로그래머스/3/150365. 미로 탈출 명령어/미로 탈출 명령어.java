import java.util.Stack;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

class Solution {
    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        if(isImpossible(x,y,r,c,k)) {
            return "impossible";
        }
        String[] min = {"d","l","r","u"};
        
        String[] move = {"d","l","r","u"};
        int[] moveY = {1,0,0,-1};
        int[] moveX = {0,-1,1,0};
        
        Stack<Integer[]> stack = new Stack<>();
        Stack<String> strings = new Stack<>();
        ArrayList<String> answers = new ArrayList<>();
        
        Integer[] startPoint = {x-1, y-1, 0};
        
        stack.push(startPoint);
        strings.push("");
        
        while(!stack.isEmpty()) {
            Integer[] cur = stack.pop();
            String curStr = strings.pop();
            int curY = cur[0];
            int curX = cur[1];
            int curK = cur[2];
            
            if(curK == k && curY == r-1 && curX == c-1) {
                // System.out.println(curStr);
                answers.add(curStr);
            }
            for(int i = 0; i < move.length; i++) {
                int nextY = curY + moveY[i];
                int nextX = curX + moveX[i];
                int nextK = curK+1;
                String nextStr = curStr + move[i];
                
                if(!isOverPoint(n-1, m-1, nextY, nextX) && 
                   !isImpossible(nextY, nextX, r-1, c-1, k - nextK))
                {
                    Integer[] temp = {nextY, nextX, nextK};
                    stack.push(temp);
                    strings.push(nextStr);
                    break;
                }
                
            }
        }
        Collections.sort(answers);
        return answers.get(0);
        
    }
    public int ab (int number) {
        return number < 0 ? number * -1 : number;
    }
    
    public boolean isImpossible (int x, int y, int r, int c, int k) {
        if(getDst(y, x, r, c) > k || (k - (ab(x-r) + ab(y-c))) % 2 != 0) {
            return true;
        }
        return false;
    }
    
    public boolean isOverPoint (int maxY, int maxX, int y, int x) {
        if(y > maxY || x > maxX || y < 0 || x < 0) {
            return true;
        }
        return false;
    }
    public int getDst (int y, int x, int r, int c) {
        return ab(x-r) + ab(y-c);
    }
}