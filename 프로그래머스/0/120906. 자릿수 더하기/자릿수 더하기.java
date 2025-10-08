import java.util.stream.*;
import java.util.*;
class Solution {
    public int solution(int n) {
        return Arrays.stream(Integer.toString(n).split(""))
            .mapToInt(Integer::parseInt)
            .reduce(0, (result, num) -> result + num);
        
    }
}