import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        return IntStream.range(0, rank.length)
            .filter(i -> attendance[i])
            .boxed()
            .sorted(Comparator.comparing(i -> rank[i]))
            .limit(3)
            .reduce(new int[]{0, 0},
                   (total, i) -> {
                       int idx = total[0];
                       int val = idx == 0 ? 10000 * i : idx == 1 ? 100 * i : i;
                       return new int[]{idx + 1, total[1] + val};
                   },
                   (a, b) -> new int[]{0, a[1] + b[1]})[1];
    }
}