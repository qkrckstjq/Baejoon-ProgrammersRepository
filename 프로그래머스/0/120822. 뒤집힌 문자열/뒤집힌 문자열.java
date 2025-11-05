import java.util.stream.*;
class Solution {
    public String solution(String my_string) {
        return IntStream.range(0, my_string.length())
            .boxed()
            .reduce("", (result, i) -> result + my_string.charAt(my_string.length() - (i + 1)),
                   (a, b) -> a + b);
    }
}