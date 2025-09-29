import java.util.*;
class Solution {
    public int solution(String[] strArr) {
        Map<Integer, Integer> answer = new HashMap<>();
        for(String str : strArr) {
            int len = str.length();
            answer.put(len, answer.getOrDefault(len, 0) + 1);
        }
        return answer.values().stream().reduce(0, (result, i) -> Math.max(result, i));
    }
}