import java.util.stream.*;
class Solution {
    public int solution(int[] arr1, int[] arr2) {
        if(arr1.length < arr2.length) {
            return -1;
        } else if(arr1.length > arr2.length) {
            return 1;
        }
        int sumA = IntStream.range(0, arr1.length).reduce(0, (total, i) -> total += arr1[i]);
        int sumB = IntStream.range(0, arr2.length).reduce(0, (total, i) -> total += arr2[i]);
        if(sumB > sumA) {
            return -1;
        } else if(sumA > sumB) {
            return 1;
        }
        return 0;
    }
}