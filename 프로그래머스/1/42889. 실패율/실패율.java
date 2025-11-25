import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        return IntStream.rangeClosed(1, N)
            .boxed()
            .sorted(
                Comparator
                    .comparingDouble((Integer stage) -> {
                        long reach = Arrays.stream(stages).filter(s -> s >= stage).count();
                        return reach == 0 ? 0.0 :
                            (double) Arrays.stream(stages).filter(s -> s == stage).count() / reach;
                    })
                    .reversed()
                    .thenComparingInt(i -> i)
            )
            .mapToInt(Integer::intValue)
            .toArray();
    }
}
