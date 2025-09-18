import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] query) {
        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < arr.length; i++) {
            queue.addLast(arr[i]);
        }
        for(int i = 0; i < query.length; i++){
            if(i % 2 == 0) {
                int remove = queue.size() - query[i] - 1;
                for(int j = 0; j < remove; j++){
                    queue.removeLast();
                }
            } else {
                for(int j = 0; j < query[i]; j++){
                    queue.removeFirst();
                }
            }
        }
        int[] answer = new int[queue.size()];
        int i = 0;
        while(!queue.isEmpty()) {
            answer[i++] = queue.getFirst();
            queue.removeFirst();
        }
        return answer;
    }
}