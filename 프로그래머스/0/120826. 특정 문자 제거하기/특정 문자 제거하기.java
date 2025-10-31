import java.util.*;
class Solution {
    public String solution(String my_string, String letter) {
        return Arrays.stream(my_string.split(""))
            .filter(s -> !s.equals(letter))
            .reduce("", (answer, s) -> answer + s);
    }
}