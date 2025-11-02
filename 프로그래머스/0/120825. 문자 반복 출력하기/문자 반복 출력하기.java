import java.util.*;
class Solution {
    public String solution(String my_string, int n) {
        return Arrays.stream(my_string.split(""))
            .reduce("", (result, s) -> result + s.repeat(n));
    }
}