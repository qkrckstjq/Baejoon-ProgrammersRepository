import java.util.stream.*;
import java.util.*;
class Solution {
    public String solution(int age) {
        return Arrays.stream(String.valueOf(age).split(""))
            .map(s -> Character.toString((char) ('a' + s.charAt(0) - '0')))
            .reduce("", (answer, s) -> answer + s);
    }
}