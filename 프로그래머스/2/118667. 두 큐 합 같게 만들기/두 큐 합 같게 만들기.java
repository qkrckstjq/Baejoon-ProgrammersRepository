import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = Arrays.stream(queue1).sum();
        long sum2 = Arrays.stream(queue2).sum();
        
        
        if((sum1 + sum2) % 2 != 0) return -1;
        
        int[] queue = new int[queue1.length + queue2.length];
        
        for(int i = 0; i < queue1.length; i++) {
            queue[i] = queue1[i];
        }
        
        for(int i = queue1.length; i < queue.length; i++) {
            queue[i] = queue2[i - queue1.length];
        }
         
        int i = 0, j = queue1.length;
        
        while(sum1 != sum2) {
            if(answer >= queue1.length * 3) return -1;
            if(sum1 > sum2) {
                sum1 -= queue[i];
                sum2 += queue[i++];
            } else {
                sum1 += queue[j];
                sum2 -= queue[j++];
            }
            answer += 1;
            
            if(i >= queue.length || j >= queue.length) return -1;
        }
        return answer;
    }
}