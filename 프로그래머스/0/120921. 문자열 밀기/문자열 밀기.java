import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(String A, String B) {
        Deque<String> dq = new ArrayDeque<>(List.of(A.split("")));
        int answer = 0;
        for (int shift = 0; shift < A.length(); shift++) {
            String cur = dq.stream().collect(Collectors.joining());
            if (cur.equals(B)) return shift;
            dq.addFirst(dq.removeLast());
        }
        return -1;
    }
}