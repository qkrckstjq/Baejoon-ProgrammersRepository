import java.util.stream.*;
class Solution {
    public int solution(String s) {
        String[] arr = s.split(" ");
        return IntStream.range(0, arr.length)
            .boxed()
            .mapToInt(i -> arr[i].equals("Z") ? Integer.parseInt(arr[i - 1]) * -1 : Integer.parseInt(arr[i]))
            .reduce(0, (result, num) -> result += num);
    }
}