import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        return IntStream.range(0, rank.length)
            .filter(i -> attendance[i])
            .boxed()
            .sorted(Comparator.comparing(i -> rank[i]))
            .limit(3)
            .reduce(0, (total, next) -> total * 100 + next);
    }
}