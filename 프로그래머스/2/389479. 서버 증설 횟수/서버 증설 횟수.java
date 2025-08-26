import java.util.*;

class Solution {
    public static void process(Deque<Integer> q) {
        int n = q.size();
        for (int i = 0; i < n; i++) {
            int v = q.removeFirst() - 1; 
            if (v > 0) q.addLast(v);
        }
    }
    
    public int solution(int[] players, int m, int k) {
        Deque<Integer> queue = new ArrayDeque<>();
        int answer = 0;
        for(int player : players) {
            process(queue);
            int need = player / m;
            int curServer = queue.size();
            int addServer = need - curServer;
            for(int i = 0; i < addServer; i++) {
                queue.add(k);
                answer += 1;
            }
        }
        
        return answer;
    }
}