import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr, int n) {
        return IntStream
            .range(0, arr.length)
            .mapToObj(i -> {
                if((arr.length % 2 == 0 && i % 2 != 0) || (arr.length % 2 != 0 && i % 2 == 0)) {
                    return arr[i] + n;
                }
                return arr[i];
            })
            .mapToInt(i -> i)
            .toArray();
    }
}