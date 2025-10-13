import java.util.*;
class Solution {
    public int solution(int order) {
        return (int) Arrays.stream(String.valueOf(order).split(""))
            .filter(s -> "369".contains(s))
            .count();
    }
}