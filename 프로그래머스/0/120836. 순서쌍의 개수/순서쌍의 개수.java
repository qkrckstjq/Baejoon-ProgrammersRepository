import java.util.stream.*;
class Solution {
    public int solution(int n) {
        return IntStream.range(1, ((int) Math.sqrt(n)) + 1)
            .reduce(0, (answer, i) -> answer + (n % i == 0 ? 1 : 0)) * 2 - ((int) Math.sqrt(n) * (int) Math.sqrt(n) == n ? 1 : 0);
    }
}