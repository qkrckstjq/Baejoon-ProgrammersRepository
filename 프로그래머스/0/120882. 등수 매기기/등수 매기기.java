import java.util.stream.*;
import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        return IntStream.range(1, score.length + 1)
            .map(i -> 1 + (int) IntStream.range(1, score.length + 1)
                .filter(j -> (score[j - 1][0] + score[j - 1][1]) > (score[i - 1][0] + score[i - 1][1]))
                .count()
            )
            .toArray();
    }
}
