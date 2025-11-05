import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        int n = emergency.length;

        Integer[] order = IntStream.range(0, n).boxed()
            .sorted(Comparator.comparingInt((Integer i) -> emergency[i]).reversed())
            .toArray(Integer[]::new);

        int[] rank = new int[n];
        for (int r = 0; r < n; r++) rank[order[r]] = r + 1;

        return rank;
    }
}
