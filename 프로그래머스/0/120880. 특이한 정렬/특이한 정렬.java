import java.util.stream.*;
import java.util.*;
class Solution {
    public int[] solution(int[] numlist, int n) {
        return IntStream.range(0, numlist.length)
            .boxed()
            .sorted(Comparator.comparing((Integer i) -> (Math.abs(numlist[i] - n))).thenComparing((Integer i) -> numlist[i] * -1))
            .mapToInt(i -> numlist[i])
            .toArray();
    }
}