import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;

        Map<String, Integer> target = new HashMap<>();

        for (int i = 0; i < want.length; i++) {
            target.put(want[i], number[i]);
        }

        for (int start = 0; start <= discount.length - 10; start++) {
            Map<String, Integer> current = new HashMap<>();

            for (int j = start; j < start + 10; j++) {
                current.put(discount[j],
                        current.getOrDefault(discount[j], 0) + 1);
            }

            if (target.equals(current)) {
                answer++;
            }
        }

        return answer;
    }
}