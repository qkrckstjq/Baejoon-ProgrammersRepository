import java.util.*;

class Solution {
    public int solution(int[][] lines) {
        final int OFFSET = 100;        // -100 보정
        int[] cnt = new int[200];      // [-100..99] → 200개 구간

        for (int[] L : lines) {
            int s = L[0], e = L[1];
            for (int x = s; x < e; x++) cnt[x + OFFSET]++;
        }

        int answer = 0;
        for (int c : cnt) if (c >= 2) answer++;
        return answer;
    }
}
