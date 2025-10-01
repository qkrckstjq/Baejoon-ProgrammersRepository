import java.util.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        Set<Integer> used = new HashSet<>();
        for(int num : delete_list) used.add(num);
        return Arrays.stream(arr).filter(num -> !used.contains(num)).toArray();
    }
}