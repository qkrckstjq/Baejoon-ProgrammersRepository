import java.util.*;

class Solution {
    public int[] solution(int[] numbers, String direction) {
        Deque<Integer> dq = new ArrayDeque<>();
        for (int x : numbers) dq.addLast(x);

        if ("right".equals(direction)) {
            dq.addFirst(dq.removeLast());
        } else {
            dq.addLast(dq.removeFirst());
        }

        int[] ans = new int[numbers.length];
        int i = 0;
        for (int x : dq) ans[i++] = x;
        return ans;
    }
}
