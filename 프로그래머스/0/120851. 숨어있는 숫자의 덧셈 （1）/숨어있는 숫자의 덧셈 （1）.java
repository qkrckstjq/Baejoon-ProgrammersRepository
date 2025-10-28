import java.util.*;
class Solution {
    public int solution(String my_string) {
        return Arrays.stream(my_string.split(""))
            .filter(s -> 0 < s.charAt(0) - '0' && s.charAt(0) - '0' <= 9)
            .mapToInt(s -> s.charAt(0) - '0')
            .reduce(0, (result, num) -> result + num);
    }
}