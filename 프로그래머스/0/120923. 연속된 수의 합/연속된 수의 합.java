import java.util.stream.*;
class Solution {
    public int[] solution(int num, int total) {
        return IntStream.range(0, num)
            .map(i -> (total / num - (num - 1) / 2) + i)
            .toArray();
    }
}