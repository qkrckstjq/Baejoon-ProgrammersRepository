import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        return IntStream.range(0, rank.length)
            .filter(i -> attendance[i])
            .boxed()                                                
            .sorted(Comparator.comparingInt(i -> rank[i]))
            .limit(3)
            .reduce(new int[]{0, 0}, (state, i) -> {
                    int idx = state[0];
                    int val = idx == 0 ? 10000 * i : idx == 1 ? 100 * i : i;
                    return new int[]{idx + 1, state[1] + val};
                },
                (a, b) -> new int[]{0, a[1] + b[1]})[1];
    }
}