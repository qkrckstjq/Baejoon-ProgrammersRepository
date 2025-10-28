import java.util.*;
class Solution {
    public String solution(String my_string) {
        return Arrays.stream(my_string.split(""))
            .filter(s -> !s.equals("a") && !s.equals("e") && !s.equals("i") && !s.equals("o") && !s.equals("u"))
            .reduce(new String(""), (result, s) -> result + s);
    }
}