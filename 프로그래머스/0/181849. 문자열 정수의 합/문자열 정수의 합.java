import java.util.stream.*;
class Solution {
    public int solution(String num_str) {
        return IntStream.range(0, num_str.length())
            .reduce(0, (total, i) -> total + (num_str.charAt(i) - '0'));
    }
}