import java.util.*;
class Solution {
    
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int i = 0; i < enemy.length; i++) {
            int curEnemy = enemy[i];
            n -= curEnemy;
            heap.offer(curEnemy * -1);
            
            if(n < 0) {
                if(k > 0) {
                    k -= 1;
                    n += (heap.poll() * -1);
                }
                if(n < 0) {
                    return i;
                }
            }
        }
        return enemy.length;
    }
}