import java.util.stream.*;
class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        return IntStream.range(num1, num2 + 1)
            .boxed()
            .mapToInt(i -> numbers[i])
            .toArray();
    }
}