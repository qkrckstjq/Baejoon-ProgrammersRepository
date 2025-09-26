import java.util.stream.*;
class Solution {
    public String[] solution(String[] strArr) {
        return IntStream.range(0, strArr.length)
            .mapToObj(i -> strArr[i])
            .filter(str -> !str.contains("ad"))
            .toArray(String[]::new);
    }
}