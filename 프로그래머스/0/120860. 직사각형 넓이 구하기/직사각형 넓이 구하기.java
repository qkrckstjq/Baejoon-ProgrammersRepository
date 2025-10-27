import java.util.*;
class Solution {
    public int solution(int[][] dots) {
        int[] row = Arrays.stream(dots)
            .reduce(new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE}, (result, arr) -> {
                result[0] = Math.min(arr[0], result[0]);
                result[1] = Math.max(arr[0], result[1]);
                return result;
            });
        int[] col = Arrays.stream(dots)
            .reduce(new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE}, (result, arr) -> {
                result[0] = Math.min(arr[1], result[0]);
                result[1] = Math.max(arr[1], result[1]);
                return result;
            });
        return (row[1] - row[0]) * (col[1] - col[0]);
    }
}