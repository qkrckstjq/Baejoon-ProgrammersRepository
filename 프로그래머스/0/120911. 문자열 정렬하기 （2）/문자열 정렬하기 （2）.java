import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String my_string) {
        return my_string.toLowerCase()
                        .chars()
                        .sorted()
                        .collect(StringBuilder::new,
                                 StringBuilder::appendCodePoint,
                                 StringBuilder::append)
                        .toString();
    }
}
