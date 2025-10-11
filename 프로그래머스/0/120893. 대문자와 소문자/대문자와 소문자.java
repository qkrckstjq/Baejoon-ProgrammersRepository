import java.util.*;
class Solution {
    public String solution(String my_string) {
        return Arrays.stream(my_string.split(""))
            .map(s -> s.toUpperCase().equals(s) ? s.toLowerCase() : s.toUpperCase())
        .reduce("", (result, s) -> result += s);
    }
}