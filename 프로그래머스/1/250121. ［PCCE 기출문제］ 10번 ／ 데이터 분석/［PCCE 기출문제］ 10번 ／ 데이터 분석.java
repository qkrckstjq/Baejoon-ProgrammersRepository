import java.util.*;
import java.util.stream.*;
class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> index = new HashMap<>();
        index.put("code", 0);
        index.put("date", 1);
        index.put("maximum", 2);
        index.put("remain", 3);
        
        return Arrays.stream(data)
            .filter(d -> d[index.get(ext)] < val_ext)
            .sorted(Comparator.comparing(a -> a[index.get(sort_by)]))
            .toArray(int[][]::new);
    }
}