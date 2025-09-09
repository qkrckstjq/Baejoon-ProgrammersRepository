import java.util.*;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
        if (l == 0) list.add(0);        // 문제에서 0을 포함한다면

        Queue<Long> q = new ArrayDeque<>();
        q.add(5L);

        while (!q.isEmpty()) {
            long x = q.poll();
            if (x > r) continue;
            if (x >= l) list.add((int)x);

            long n0 = x * 10;
            long n5 = x * 10 + 5;
            if (n0 <= r) q.add(n0);
            if (n5 <= r) q.add(n5);
        }

        if (list.isEmpty()) return new int[]{-1};
        int[] ans = new int[list.size()];
        for (int i = 0; i < list.size(); i++) ans[i] = list.get(i);
        return ans;
    }
}
