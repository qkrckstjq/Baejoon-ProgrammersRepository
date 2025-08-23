import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>(
            Comparator.comparingInt(a -> a)
        );
        for(int s : scoville) {
            queue.offer(s);
        }
        
        while(queue.peek() < K) {
            if(queue.size() < 2) {
                return -1;
            }
            Integer first = queue.poll();
            Integer second = queue.poll();
            queue.offer(first + second * 2);
            answer += 1;
        }
        
        return answer;
    }
}