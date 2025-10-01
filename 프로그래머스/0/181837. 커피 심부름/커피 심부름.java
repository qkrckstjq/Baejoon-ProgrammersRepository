import java.util.*;
class Solution {
    public int solution(String[] order) {
        return Arrays.stream(order)
            .reduce(0,
                    (result, str) -> result + (str.contains("americano") || !str.contains("latte") ? 4500 : 5000), 
                    (a, b) -> a + b);
    }
}