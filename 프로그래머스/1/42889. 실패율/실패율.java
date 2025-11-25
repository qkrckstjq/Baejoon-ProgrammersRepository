import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int N, int[] stages) {
        Arrays.sort(stages);
        double[] result = new double[N + 1];
        double prev = 0;
        for(int i = 0; i < stages.length; i++) {
            if(stages[i] > N) break;
            int cur_s = stages[i];
            double user = 0;
            double total = stages.length;
            while(i < stages.length && cur_s == stages[i]) {
                i++;
                user++;
            }
            i--;
            // System.out.printf("%d 스테이지 도달한 사람 %f, 실패한 사람 %f\n", cur_s, total - prev, user);
            result[cur_s] = user / (total - prev);
            prev += user;
        }
        // for(double r : result) System.out.println(r);
        return IntStream.range(1, N + 1)
        .boxed()
        .sorted(
            Comparator.comparingDouble((Integer i) -> result[i] * -1)
                      .thenComparingInt(i -> i)                 
        )
        .mapToInt(Integer::intValue)
        .toArray();
    }
}